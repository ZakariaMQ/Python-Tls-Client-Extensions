import tls_client

from exts.browser_profiles import BrowserProfileUtil

profile = BrowserProfileUtil() # the profile is already generated

session = tls_client.Session(
    client_identifier=profile.browser_profile.client_identifier,
    random_tls_extension_order=True,
)

r = session.get("https://httpbin.org/headers", headers=profile.browser_profile.headers)
print(r.json())