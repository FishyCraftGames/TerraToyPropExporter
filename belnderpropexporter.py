import bpy
import mathutils

exportTXT=open('C:\\export.txt','w')

exportTXT.write("@category 2"+"\n"+"@placesound 4"+"\n"+"@rotateable"+"\n"+"\n")

for obj in bpy.context.scene.objects: 
            if obj.type == 'MESH': 
                posx = round(obj.location.x, 3)
                posy = round(obj.location.z, 3)
                posz = round(obj.location.y, 3)
                pos = str(posx)+","+ str(posy)+","+ str(posz)
                
                scalex = round(obj.scale.x, 3)
                scaley = round(obj.scale.z, 3)
                scalez = round(obj.scale.y, 3)
                scale = str(scalex)+","+str(scaley)+","+str(scalez)
                
                rotx = round(obj.rotation_euler.x, 3)
                roty = round(obj.rotation_euler.z, 3)
                rotz = round(obj.rotation_euler.y, 3)
                rot = str(rotx)+","+str(roty)+","+str(rotz)
                
                material = obj.active_material
                inputs = material.node_tree.nodes["Principled BSDF"].inputs
                color = inputs["Base Color"].default_value
                colorOUT = str(round(color[0]*255,1))+","+str(round(color[1]*255,1))+","+str(round(color[2]*255,1))
                colorOUTdark = str(round(color[0]*255*0.8,1))+","+str(round(color[1]*255*0.8,1))+","+str(round(color[2]*255*0.8,1))
                
                material = "MAT_MATTE"
                transformModifier = "TF_NONE"
                
                roughness = inputs["Roughness"].default_value
                emission = inputs["Emission Strength"].default_value
                transmission = inputs["Transmission"].default_value
                subsurface = inputs["Subsurface"].default_value
                
                if roughness < 0.5:
                    material = "MAT_REFLECTIVE"
                if emission > 1:
                    material = "MAT_EMISSIVE"
                if transmission > 0:
                    material = "MAT_TRANSPARENT"
                if color[3] < 1:
                    material = "MAT_EMPTY"
                if subsurface > 0:
                    material = "MAT_LEAVES"
                    transformModifier = "TF_LEAVES,vec3("+colorOUT+"),vec3("+colorOUTdark+")"
                                    
                exportTXT.write("box("+ material +", vec3("+ colorOUT +"), vec3("+ pos +"),vec3("+ scale +"),quaternion(vec3("+ rot +")), "+ transformModifier +")"+"\n")
                
exportTXT.close()