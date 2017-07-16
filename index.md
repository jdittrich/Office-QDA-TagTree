# QDA Tag Tree for LibreOffice

…Qualitative Data Analysis is not easy. And if you don't want to spend a large amount of money, you are back to very basic methods when you code your data. Many people use word processors for analysis as a wide spread and affordable alternative. 

QDA Tag tree builds on that and enhances LibreOffice with a Sidebar function that allows you to view all your codes.

![Screenshot of the extension; shows Libreoffice comments and a tree view](http://i.imgur.com/7k9Meb6.png)

The codes are written in the standard comments, so source text and codes can stay separate. 

## Use
**Create comments**  Mark a text you want to code and create a comment (Ctrl+Alt+C)


**Writing Codes** Assign your codes: Just write a *#Hashtag* in the comment. QDA Tag Tree will recognize these as codes. The content of a comment can thus look like this: 

> #fun #analysis 

You can also put other text in it: 

> #fun #analysis Note to self: Is fun the right code here? I think we might want to discuss it's definition. 

You can also create sub codes that will show as child codes in the tree: 

> #fun #analysis#review

Which will create a tree-group with text-sections coded with #fun and another tree-group #analysis with a child group #review. This way you can keep the overview. 


**Don’t forget to press *update* to, well, update the tag tree.** 

**Review Codes:** If you click on an item in the tree that represents coded text (the ones without a fold/unfold icon and a *#*) you can see the coded text in the upper part of the panel. If "jump to clicked Tag" is checked, it will  scroll the document to the coded text. 

## Meta

**License:** *QDA Tag Tree* is Open Source Software. Its code is licensed under GPL3.

**Thanks**
Scaffold code was generated using [unodit](https://github.com/kelsa-pi/unodit). This projects would not have been possible without using unodit.

