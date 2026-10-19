import maya.cmds as cmds

cmds.delete(cmds.ls("cube_*", type="transform"))

for i in range(5):
    cube = cmds.polyCube(
        name=f"cube_{i}",
        width=1,
        height=6,
        depth=1
    )[0]

    cmds.move(i * 3, 3, 0, cube)
    cmds.rotate(0, 0, 0, cube)

for i in range(2):
    cube = cmds.polyCube(
        name=f"cube_{i}",
        width=15,
        height=0.7,
        depth=0.7
    )[0]

    cmds.move(7.5, i * 3 + 1.5, 0, cube)
    cmds.rotate(0, 0, 0, cube)