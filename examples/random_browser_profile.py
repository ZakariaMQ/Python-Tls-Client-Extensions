from pprint import pprint
import tls_client
import sys

sys.path.append("../")

from exts.browser_profiles import BrowserProfileUtil

profile = BrowserProfileUtil() # the profile is already generated
client_identifier = profile.browser_profile.client_identifier # random identifier has been picked
headers = profile.browser_profile.headers # the appropriate headers have been picked and the matching user agent as well

session = tls_client.Session(
    client_identifier=client_identifier,
    random_tls_extension_order=True,
)

r = session.get("https://httpbin.org/headers", headers=headers)
pprint(r.json()["headers"])
