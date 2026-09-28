import maya.cmds as cmds

cmds.window(
    title="Du texte en pop up", 
    widthHeight=(300, 100)
)
cmds.columnLayout(
    adjustableColumn=True,
    rowSpacing=5,
    columnOffset=("both",20)
)
cmds.popupMenu()
cmds.text("du texte")
cmds.text("woah des marges")
cmds.showWindow()