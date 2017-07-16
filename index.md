# QDA Tag Tree for LibreOffice

…Qualitative Data Analysis is not easy. And if you don't want to spend a large amount of money, you are back to very basic methods when you code your data. Some people [use word processors for analysis](https://www.slideshare.net/jennacondie/working-with-word-for-qualitative-data-analysis) as a wide spread and affordable alternative. 

*QDA Tag Tree* builds on that and enhances [LibreOffice Writer](http://www.libreoffice.org/) (a free word processor): It adds a sidebar that allows you to view all your codes (also called *tags* here, since they are written as *#hashtags*).

![Screenshot of the extension; shows LibreOffice comments and a tree view](http://i.imgur.com/7k9Meb6.png)

The codes are written in the standard comments, so transcribed text and codes can stay separate. 

## Download and installation

**[🡇 QDA Tag Tree Release](https://github.com/jdittrich/Office-QDA-TagTree/releases/latest)**

Requires [LibreOffice Writer](http://www.libreoffice.org/) 5.3


1. Download the .oxt file from the link above (not the .zip or .tar)
2. Double click the .oxt file to install it
3. Restart LibreOffice Writer


## Use
**Open *QDA tag tree* ** Open LibreOffice writer and click on the QDA Tag tree icon in the sidebar (usually at the right side of the writer window): ![QDA Tag Tree icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACEAAAAjCAIAAACVTvQzAAAAA3NCSVQICAjb4U/gAAAAGXRFWHRTb2Z0d2FyZQBnbm9tZS1zY3JlZW5zaG907wO/PgAAAnVJREFUSIntls1rE0EYxp/Z3SRtPgQ1FvFk9i/wJqiQS0EERb2U4kcVDyoeeuuh4sFDL0o8FhrqUbRiQRA8CH7gZ0QPIhSlYnoSQUq1Kmx2NjPzesgmbpJJdtNY8NCHMMzOzs5v5nnfmQn79XMV6yxjvQEbjP+OYWlbSUkhnOijGGbCNOM9MKRwn98fd35/A2NBrnYyAEBkWgP7R+9EZ9C7F1e3ZLcdHBkHCUCABCDrdUl+iwBJQACi6lXu3r7XeZFt8fj0/pbrfN2dHwEpQDWVUICsV+p1/1U3Na2Du6ufF+YOjV40TcPj7qnz03WLqP5DsFIsDGfSRm8MJauWNTiYzIBEPG7cvH4BAWcIrdYx1Oq9MMAYQA1nGNM5wwKl75U2HTowYrGkkPzHypfNW4dA6vjZohRKZ5SfTsVr+U1pA1Csq11NDCuW3LVn4umD6QNHzyUGEjeKZ0j5zlAjkQJJZbBai6Kue7k1d3fs3Pd9eeHVo/m9w0fgB0AF8lXhb1RUrVF4nHUNCWu/P0jJNw8vrSx/aDQ0Cp0IQCqzPX94tgfGP1fImUhEpdJLIiIi1aaIDP2ZGGR8XFzMZoeePHsshGh5O3bidDqV6pcBgFc927Zfvy2JaiuDNR2aa2UQUZV7AE4eG4synFbhdxTnHJGm21HhXnmet1ReMgx/NnPzc+2BqWlyYjIe19xUkRi2bZumWXusVCpSSm1P6rCJIjGCj1OXp0I/aVFoPIhz3uugLQpdB/M8r1wuN7yamZ1xXVfbtXClkEgk1sAA93gul7Msv6fruo6j/8tCpI9H+HnlOE4ymQydSheF748+AZEY/WuDEV1/AKwnbSrLZY32AAAAAElFTkSuQmCC)

You won’t see anything interesting yet, because you have not coded your data, yet. 

**Create comments:**  Mark a text you want to code and create a comment (Ctrl+Alt+C)

**Writing Codes:** Assign your codes: Just write a *#Hashtag* in the comment. QDA Tag Tree will recognize these as codes. The content of a comment can thus look like this: 

> #fun #analysis 

Other text in comments with the #hashtags works, too: 

> #fun #analysis Note to self: Is fun the right code here? I think we might want to discuss its definition. 

You can also create sub codes that will show as child codes in the tree: 

> #fun #analysis#review

Which will create a tree-group with text-sections coded with #fun and another tree-group #analysis with a child group #review. This way you can keep the overview. 


**Don’t forget to press *update* to update the tag tree.** 

**Review Codes:** If you click on an item in the tree that represents coded text (the ones without a fold/unfold icon and a *#*) you can see the coded text in the upper part of the panel. If "jump to clicked Tag" is checked, it will  scroll the document to the coded text. 

## Meta

**License:** *QDA Tag Tree* is Open Source Software. Its code is licensed under GPL3.

**Thanks**
Scaffold code was generated using [unodit](https://github.com/kelsa-pi/unodit). This projects would not have been possible without using unodit.

