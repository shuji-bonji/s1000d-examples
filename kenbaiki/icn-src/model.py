# 3D のモデル（ICN-K0001-00006-001-01.STEP）を作る。CadQuery 2.8.0（Open CASCADE）で実行する。
import cadquery as cq

body = cq.Workplane("XY").box(600, 400, 1500)
door = cq.Workplane("XY").box(560, 20, 1100).translate((0, -210, 100))
handle = cq.Workplane("XY").box(30, 30, 160).translate((230, -235, 100))

asm = cq.Assembly(name="kenbaiki")
asm.add(body, name="cabinet", color=cq.Color(0.8, 0.8, 0.82))
asm.add(door, name="front-door", color=cq.Color(0.2, 0.4, 0.8))
asm.add(handle, name="door-handle", color=cq.Color(0.9, 0.6, 0.1))
asm.export("ICN-K0001-00006-001-01.STEP")
