"""First time client opened"""

from pages.mainPage import QpcInternalURL

def test_general_settings_first_enter(browser):
    general_settings = QpcInternalURL(browser)
    url = "http://192.168.110.13:8091/Qa/ManagementLayer/index.html#/installations/QPC/Applications"

    # Given the DuckDuckGo home page is displayed
    #general_settings.load()

    # When the user searches for "panda"pip
    #general_settings.search(QpcInternalURL)

    # Then the search result title contains "panda"
    #assert QpcInternalURL in result_page.title()

    # And the search result query is "panda"
    #assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    #titles = result_page.result_link_titles()
    #matches = [t for t in titles if PHRASE.lower() in t.lower()]
    #assert len(matches) > 0

    ### TODO: Remove this exception once the test is complete
   # raise Exception("Incomplete Test")

