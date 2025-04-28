---
title: "Headphone Stand"
excerpt: "Generative designed headphone stand"
header:
  image: /assets/img/Syringe_Pump_Rendering_2.png
  teaser: /assets/img/Syringe_Pump_Rendering_2.png
gallery:
  - image_path: assets/img/Syringe_Pump_Real_Life_1.jpg
  - image_path: assets/img/Syringe_Pump_Rendering_1.png
  - image_path: assets/img/Syringe_Pump_Rendering_2.png
---

## Overview

The generative designed part for this project is a Mandalorian (from Star Wars) themed headphone stand. When shopping for headphone stands, an feature I frequently observe on commercial headphone stands is a supporting rod that protrudes from the center of the stand's base. At resting position, headphones' earcups The inconvenient location of this rod necessitate the earcups of the headphones to be pried open when placing the headphones on the stand, which makes the single-hand operation of placing the headphones on the stand an inconvenient task. Consequently, since the earcups clamp down on the supporting rod, taking the headphones off the stand with a single hand is an equally challenging task, as the stand would move along with the headphones due to friction. The headphone stand designed in this project aims to overcome this limitation, making it easy to place and remove headphones from the stand with a single hand, while incorporating symbolic elements of Mandalorian culture to make the stand a Star Wars fan favorite.

## Preserve and Obstacle Geometries

There are four preserve geometries in the generative design model. The headband support is a curved plate on which the headband of the headphones will rest. The curvature of the support plate is less that that of the headband, allowing the support plate to cause deformations in the foam headband, providing friction that prevents the headphones from wobbling on the stand. The Mandalorian Din Djarin's famous phrase "This is the way" is debossed on the support plate, adding a touch to the Mandalorian theme. 

## **Operating Procedure**

1. Fill the syringe with liquid and insert into the holders. 
2. Fit the 20 mL syringe into the protruding back slot or the 10 mL syringe into the front slot. 
3. Make sure the ON/OFF button next to the LED light is pressed in, indicating an OFF stage. Plug in the power cord. The LED turns yellow. 
4. If a preset flow rate is desired, adjust the potentiometer such that it outputs “Flow Rate: 0” (completely turned to the left) or “Flow Rate: 100” (completely turned to the right). Then press the ON/OFF button to start the device at a consistent preset speed. 
5. If the potentiometer is required for operation, start with the knob turned completely to the left or the right (0 or 100 Flow Rate), press the ON/OFF button to start the device, and then adjust the knob to a desired flow rate such that the potentiometer is activated to control the speed of the motor. 
6. The LCD displays the flow rate and the time countdown. 
7. The LED turns green when the device is running, turns yellow when the flow rate is 0 and there’s liquid remaining in the syringe, and turns red when the device reaches the end of its operation. 

## **Required Parts**

- **3D Printed Parts**

| Part Name | Quantity |
| --- | --- |
| Enclosure Shell | 1 |
| Enclosure Drawer | 1 |
| Syringe Support | 1 |
| Plunger Support | 1 |
| Carriage | 1 |

- **Off-the-shelf Parts**

| Part Name | Quantity |
| --- | --- |
| Latching Push Button (9.5 mm)| 1 |
| Flexible Coupling (1/4" x 8 mm) | 1 |
| Flanged Ball Bearing | 1 |
| Potentiometer with Knob | 1 |
| LCD Screen | 1 |
| Lead Screw (250 mm with 2 mm pitch) | 1 |
| LED | 1 |
| Linear Rod (200 mm x 8 mm) | 1 |
| Linear Bearing (8 mm bore diameter) | 1 |
| Lock Collar - Lead Screw | 1 |
| Lock Collar - Linear Rod | 1 |
| M3 x 8 mm Thread Forming Screw | 4 |
| M3 x 10 mm Bolt | 4 |
| M5 x 8 mm Bolt | 6 |
| T-Nut | 6 |
| NEMA 17 Stepper Motor | 1 |
| Aluminum Extrusion 20 mm x 40 mm x 350 mm | 1 |
| Power Supply | 1 |
| Arduino Uno | 1 |
| Stepper Driver (Microcontroller) | 1 |
| Small Breadboard | 1 |
| Limit Switch | 1 |

## **Supplementary Files**

- [Python flow rate calculator](https://github.com/aaron-xu1009/aaron-xu1009.github.io/blob/main/_data/Flow_Rate_Calc.py)

- [Arduino code](https://github.com/aaron-xu1009/aaron-xu1009.github.io/blob/main/_data/Arduino_Code.ino)

## **CAD Model**
<iframe src="https://vanderbilt643.autodesk360.com/shares/public/SH512d4QTec90decfa6e1faab3ee761fd268?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>

{% include gallery caption="Syringe Pump" %}
