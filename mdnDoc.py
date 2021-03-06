import sublime_plugin
import re
import sublime
import webbrowser


PATTERN = re.compile(r'([a-z-]+)', re.IGNORECASE)
URL_DOMAIN = 'https://developer.mozilla.org/'
URL_SEARCH = '/search?q='

class MdnDocCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        #get settings
        settings = sublime.load_settings('MdnSearchDoc.sublime-settings')
        language_settings = settings.get("language")

        if len(language_settings) == 0:
            LANGUAGE = "en-US"
        else:
            LANGUAGE = language_settings

        #each of selections
        for region in self.view.sel():
            # Get the start point of the region of the selection
            point = region.begin()
            scope = self.view.extract_scope(point)
            search = self.view.substr(scope)

            # CSS ------------------------------------------------
            if "/CSS" in self.view.settings().get('syntax'):
                # Clean the selection on css syntax
                re_search = PATTERN.search(search)
                if re_search:
                    search = re_search.group()
                search = search + '&topic=css'

            # Javascript -----------------------------------------
            if "/JavaScript" in self.view.settings().get('syntax'):
                search = search + '&topic=js'

            # HTM ------------------------------------------------
            if "/HTML" in self.view.settings().get('syntax'):
                search = search + '&topic=html'

            print(webbrowser._tryorder)
            print(webbrowser._browsers.items())
            webbrowser.open_new_tab(URL_DOMAIN + LANGUAGE + URL_SEARCH + search)
