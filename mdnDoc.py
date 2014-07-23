import sublime_plugin
import re
import webbrowser


PATTERN = re.compile(r'([a-z-]+)', re.IGNORECASE)
URL = 'https://developer.mozilla.org/en-US/search?q='


class MdnDocCommand(sublime_plugin.TextCommand):

    def run(self, edit):
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
            webbrowser.open_new_tab(URL + search)
