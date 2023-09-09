# ![logo-export](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/0d45786f-fefd-407b-b103-c2a48f732ed0)
### Content:
-Important Infos 

-Materials

-Exporting

## Important Info
This is an unofficial blender addon script that exports your blend scene to a .txt file. It also exports the materials, more abput that later. For now it can only export cubes so make sure to model using cubes only. You will need the official Terra Toy Prop Tool: https://github.com/frozein/Terra-Toy-Prop-Tool to turn your .txt into a .prop file and only the .prop file is accepted by the game.
### ![Screenshot 2023-09-09 182128](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/5067ae6f-7e14-444b-991c-b0094a3f499c)
Cubes should be **larger then 1,1,1** as they will be too small to be visible in terra toy otherwise! Make sure your **scale is positive** as negative values are not supported by terra toy and therefore will not work !!!

## Materials
### Basic Material
The image below shows the node set up in blender for a Basic Material, note that adding nodes to this set up might break the exporter. This applies to all materials. changing the base color changes the objects color. Terra doy displays the colors way darker then blender so you shouldnt make them too dark
### ![BaseMat](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/43e38255-60d5-4908-a9ca-1c3faa3f141d) ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/0289ce8e-7949-4af5-bc2f-ec426d31f7c7)

### Reflective Material
Decreasing the roughness to a value below 0.5 makes the material shiny.
### ![Screenshot 2023-09-09 183502](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/adc39d16-979d-420c-8d21-f1380d0cfe72) ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/26b265c2-5119-4037-af79-2a3ff582bf96)

### Glowing Material
Increase the Emission to a value above 1 and your material will glow. the material will always glow with the same strength no matter how high you set it in blender. The base color is still responisble for the glow color, the emmision color in blender doesnt matter. Emmisive materials in Terra toy are quite dark so decrease the base colors saturation for a "brighter" looking light source.
### ![Screenshot 2023-09-09 183709](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/121aca2d-c5c7-472a-a6e6-692fca013aa4)

### Grass/Leave Material
The grass material can be used for many more things other then grass and leaves, such as a thatch roof. To use the grass material simply increase the Subsurace scattering value in blender.
### ![Screenshot 2023-09-09 185031](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/971a4776-a83b-4fb0-be3c-a5d8ef149a8f) ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/27ef92da-d1e3-494e-822b-cea373bd2243)

### Invisible Material
used for invisible objects to cut stuff out ouf other cubes like in the side of this cathedral. To do this simply decrease the Base colors alpha below a value of 1.
### ![Screenshot 2023-09-09 183816](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/238333af-fdd1-42d0-bdb0-4aacf7e4d1e3) ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/7249712e-8b11-4608-919b-7d677da1051c)

## Exporting
To export head over to the script section in blender
### ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/77e35f87-d5b1-4036-b489-2213b7575152)
then open the blenderpropexporter.py
### ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/bc516c80-dbe4-428f-8f65-cc76c1ee1f1d)
after loading the exporter you can run the script by clicking this button
### ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/2d3fdbd2-e0e2-4d15-9f78-79e97f2eec32)
this creates a .txt file that you can now turn into a .prop file using the official Terra Toy Prop Tool: https://github.com/frozein/Terra-Toy-Prop-Tool
If You get an error in blender(in the bottom left) taht looks like this:
### ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/5911605d-883b-4660-9ccd-31f61200f967)
you need to change the output in line 4 to a difrent drive or folder that is not read-only. A usb stick usually works fine or a difrent hard drive then C
### ![image](https://github.com/FishyCraftGames/TerraToyPropExporter/assets/88033703/c5f2ff85-e1a5-4605-803e-ebacd93edb29)

Thank you for using the prop exporter
