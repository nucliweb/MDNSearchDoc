MDN Search Doc
==============

Sublime Text MDN Search Doc is a plugin allows you to consult the documentation in the Mozilla Developer Network [MDN](https://developer.mozilla.org/)


Installation
------------

Use the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) and search for MDN Search Doc

or

Copy the python file to your Packages/User Folder.
Add this line to the User Keybindings

    { "keys": ["ctrl+alt+m"], "command": "mdn_doc" }


Usage
-----

Mark or place your cursor over a property and use the shortcut "ctrl+alt+m" or right click for context menu and select MDN Search Doc... to open a new tab on you web browser with the info.

![](https://raw.github.com/nucliweb/MDNSearchDoc/master/images/context-menu.png)

Tip: Use multiple selection to display info on all selected elements.


FAQ
---

1. How can I change shortcut?

	Go to:

    ```
    Sublime Text  -> Preferences -> Package Settings -> MDN Search Doc -> Key Bindings - User
    ```

    ```
	[
	    {
	        "keys": ["ctrl+alt+m"], "command": "mdn_doc"
	    }
	]
    ```


2. How to change the default language for search in MDN?

    ```
	Sublime Text -> Preferences -> Package Settings -> MDN Search Doc -> Settings - User
    ```

	and add:
    
    ```
	{
    	"language"   :  "en-US"
	}
    ```

    ###Avalaible languages on Mozilla Developer Network
	ar - عربي

	bn-BD - বাংলা (বাংলাদেশ)

	ca - català

	cs - Čeština

	de - Deutsch

	el - Ελληνικά

	en-US - English

	es - Español

	fa - فارسی

	fi - suomi

	fr - Français

	fy-NL - Frysk

	ga-IE - Gaeilge (Éire)

	he - עברית

	hi-IN - हिन्दी (भारत)

	hr - Hrvatski

	hu - Magyar

	id - Bahasa Indonesia

	it - Italiano

	ja - 日本語

	ka - ქართული

	ko - 한국어

	ml - മലയാളം

	ms - ﺐﻫﺎﺳ ﻡﻼﻳﻭ

	nl - Nederlands

	pl - Polski

	pt-BR - Português (do Brasil)

	pt-PT - Português (Europeu)

	ro - română

	ru - Русский

	sq - Shqip

	ta - தமிழ்

	th - ไทย

	tr - Türkçe

	vi - Tiếng Việt

	zh-CN - 中文 (简体)

	zh-TW - 正體中文 (繁體)


Contact
-------
Joan Leon

<joan.leon@gmail.com>

[@nucliweb](https://twitter.com/nucliweb)



Thanks
------
MDN Search Doc it's inspired in [Sublime Text Caniuse](https://github.com/Azd325/sublime-text-caniuse) by Tim Kleinschmidt <tim.kleinschmidt@gmail.com>
