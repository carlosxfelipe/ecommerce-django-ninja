from django.test import TestCase


class AuthFlowTests(TestCase):
    def test_register_login_me(self):
        r = self.client.post(
            "/api/accounts/register",
            {"email": "Carlos@Example.com", "password": "S3nh@Forte!2026"},
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 201, r.content)
        self.assertEqual(r.json()["email"], "carlos@example.com")

        dup = self.client.post(
            "/api/accounts/register",
            {"email": "carlos@example.com", "password": "S3nh@Forte!2026"},
            content_type="application/json",
        )
        self.assertEqual(dup.status_code, 409)

        r = self.client.post(
            "/api/token/pair",
            {"email": "carlos@example.com", "password": "S3nh@Forte!2026"},
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 200, r.content)
        access = r.json()["access"]
        refresh = r.json()["refresh"]

        r = self.client.get(
            "/api/accounts/me", headers={"Authorization": f"Bearer {access}"}
        )
        self.assertEqual(r.status_code, 200, r.content)
        self.assertEqual(r.json()["email"], "carlos@example.com")

        # Test token refresh (with rotation)
        ref_res = self.client.post(
            "/api/token/refresh",
            {"refresh": refresh},
            content_type="application/json",
        )
        self.assertEqual(ref_res.status_code, 200, ref_res.content)
        new_refresh = ref_res.json().get("refresh", refresh)

        # Test logout / token blacklist
        blacklist_res = self.client.post(
            "/api/token/blacklist",
            {"refresh": new_refresh},
            content_type="application/json",
        )
        self.assertEqual(blacklist_res.status_code, 200, blacklist_res.content)

        # Blacklisted refresh token should no longer work
        reuse_res = self.client.post(
            "/api/token/refresh",
            {"refresh": new_refresh},
            content_type="application/json",
        )
        self.assertEqual(reuse_res.status_code, 401)

        # Unauthenticated request rejected
        self.assertEqual(self.client.get("/api/accounts/me").status_code, 401)

    def test_wrong_password(self):
        self.client.post(
            "/api/accounts/register",
            {"email": "a@b.com", "password": "S3nh@Forte!2026"},
            content_type="application/json",
        )
        r = self.client.post(
            "/api/token/pair",
            {"email": "a@b.com", "password": "errada"},
            content_type="application/json",
        )
        self.assertEqual(r.status_code, 401)
