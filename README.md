**The Project is currently unmaintained.**


A libre office addon that finds comments that have #hashtags in them. It shows all these comments in a tree control in the sidebar (after the user pressed the update button). 

![Screenshot of the extension; shows Libreoffice comments and a tree view](http://i.imgur.com/7k9Meb6.png)

**Use**

* Open document with the text you want to analyze
* Mark sections, create comments on them (Ctrl+Alt+C)
* Write your codes as hashtags, like #fluffy
 * you can also write subcodes, using the # syntax: fluffy#unicorns will generate a subtag *unicorn* below *fluffy*
* Click on **update** in the QDA Tag Tree panel
* Tree will be generated at the lower two thirds of the panel
 * If you click on a section (not a tag), the marked text the hashtagged comment is referring to will be shown in the upper part of the panel.
 * If the option is selected, a click will also scroll the document to that text.


**State**: Alpha

**Build it:** To build it, just zip the content and change the file extension to *oxt* – which makes this a Libreoffice Extension which you can install. 



**License:** Code under GPL3

Scaffold code was generated using [unodit](https://github.com/kelsa-pi/unodit). This would not have been possible without its use.
