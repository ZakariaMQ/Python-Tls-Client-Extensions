import random
from dataclasses import dataclass

from consts.headers import (FIRFOX_HEADERS, 
                            CHROME_HEADERS, 
                            OPERA_HEADERS)
from consts.identifiers import(SUPPORTED_IDENTIFIERS, 
                                IDENTIFIERS_WITH_UA)

@dataclass
class BrowserProfile:
    client_identifier: str
    user_agent: str
    headers: dict

class BrowserProfileUtil:
    def __init__(self):
        self.supported_inderntifiers = SUPPORTED_IDENTIFIERS
        self.inderntifiers_with_ua = IDENTIFIERS_WITH_UA
        self.firefox_header = FIRFOX_HEADERS
        self.chrome_headers = CHROME_HEADERS
        self.opera_header = OPERA_HEADERS
        self.browser_profile = self.get_random_profile()

    def get_random_profile(self) -> BrowserProfile:
        identifier = random.choice(self.supported_inderntifiers)
        ua = self.inderntifiers_with_ua[identifier]
        
        if "firefox" in identifier:
            headers = self.firefox_header.copy()
        elif "chrome" in identifier:
            headers = self.chrome_headers.copy()
        else:  # opera
            headers = self.opera_header.copy()
        
        headers["User-Agent"] = ua
        
        return BrowserProfile(
            client_identifier=identifier,
            user_agent=ua,
            headers=headers
        )
