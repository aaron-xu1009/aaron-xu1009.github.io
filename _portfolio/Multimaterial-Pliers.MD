---
title: "Multimaterial Pliers"
excerpt: "Print-in-place pliers for picking up resistors"
header:
  image: /assets/img/Pliers_Header.jpg
  teaser: /assets/img/Pliers_Real_Life.jpg
gallery:
  - image_path: assets/img/Pliers_Real_Life.jpg
  - image_path: assets/img/Pliers_Credit.jpg
  - image_path: assets/img/Pliers_Header.jpg
  - image_path: assets/img/Pliers_Iteration1.jpg
  - image_path: assets/img/Pliers_Side.jpg
  - image_path: assets/img/Pliers_Iteration2.jpg
  - image_path: assets/img/Pliers_Alt_Config.jpg
---

## **Introduction**

Print-in-place models are multiplecomponent designs that work immediately after printing, requiring no post-printing processing. This is achievable through single material extrusion, but the models have to be carefully designed to allow for motion or rotation. When filament printing, these single material designs would also have to be properly oriented and print settings carefully tuned. Even with these caveats outmaneuvered, single material extrusion still face its limitations due to irregularities of plastic extrusion, and material wearing away or degrading caused by friction. Since filament printing is capable of utilizing different thermoplastics, a potential alternative would be to use multiple materials. A rigid plastic, such as TPU or ABS, could be used to print a part requiring strong mechanical properties, while an elastomer, such as TPU, could be used to print parts involved in motion or where higher friction is required. Some commercial 3D printers now offer [upgrade kits](https://www.prusa3d.com/product/original-prusa-mmu3-upgrade-kit-for-mk3s-6/) that allow multiple filaments to be used on the same print bed, allowing a print-in-place model to be created with multiple materials. In real life, multimaterial printing has been used to print [toys](https://www.youtube.com/watch?v=_vFLbze1DHM), and even create [thick-panel origamis](https://www.nature.com/articles/s41467-023-37343-w) capable of supporting heavy loads.

This project aims to leverage filament printers' ability of printing different thermoplastics to create a print-and-use needle nose plier capable of gripping and picking up through-hole resistors, where no tools are required for post printing assembly. As FFF 3D printers are capable of printing PLA and TPU filaments, the pliers would consist of rigid handles printed with PLA, and a spring component printed with TPU 95A. For ease of use, the spring component would be designed such that the pliers are returned to the open position whenever not in use, so no finger motion is required to open the plier jaws.

![Multimaterial Pliers](/assets/img/Pliers_Credit.jpg)

## **Design**

<iframe src="https://vanderbilt643.autodesk360.com/shares/public/SH286ddQT78850c0d8a4be490e3ce2235985?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>

- **Design Rationale**

Since the targeted application for the pliers is to pick up small items such as through-hole resistors, I renounced the "traditional" plier design consisting of two rigid handle fragments and two claw fragments connected to a flexible spring component and instead aimed for a design that is much more simplistic but proven to be more effective. My miniscule design is much faster to print, and reduces the amount of hand action required to close the jaws, greatly increasing operating efficiency. The design essentially combines the gripping jaw and the handle piece, reducing the required parts from 5 to 3. Grooves are added to the jaw to lock the resistor in a tight grip, preventing resistors from falling out. The spring-open motion is enabled by the flexible spring between the two handles that is printed with TPU. The spring is assymmetrically designed so that the compressive motion is preferentially directed to the jaws. Though not shown in the CAD model, a grid structure that allows for compression of the spring component is generated in Superslicer (see print settings section). The spring is held between the handles using a press-fit mating mechanism. When assembled, the duck tails on the spring piece locks the three components in place.

![Pliers at work](/assets/img/Pliers_Working.gif)

- **Print Settings**

The spring component was printed using TPU 95A with a 0.6 mm nozzle. The grid compression structure was created using the monotonic infill pattern in Superslicer. Under the **Perimeters & Shell** tab, the *Horizontal Shell* top and bottom solid layers were set to 0, and the *Vertical Shell* perimeter was set to 4. Under the **Infill** tab, the infill pattern was set to monotonic, and infill density was set to 23%. Under the **Width & Flow** tab, the infill extrusion width was set to 1.2 mm.

![Pliers at work](/assets/img/Pliers_Spring_Sliced.png)

The handles were printed using PLA with a 0.6 mm nozzle under default print settings.

- **Iterative Process**

The first iteration of the multimaterial pliers was 7 mm thick. This proved to be too thin for gripping purposes, as the spring component frequently buckled when under stress. Also, the first iteration did not include grooves on the jaw portion, causing resistors to occasionally spring out of the jaws when too much force is applied. This propmted the inclusion of positioning grooves on subsequent iterations.

![Iteration 1](/assets/img/Pliers_Iteration1.jpg)

![Side Comparison](/assets/img/Pliers_Side.jpg)

For the second iteration, the thickness of the pliers (handles and spring) was increased to 10 mm. This thickness proved to be sufficient. However, the clearance between the spring and handles was set to 0.1 mm, causing the fit to far too loose. Also, the spring's verticle perimeter thickness of 3 layers resulted in more flex than necessary.

![Iteration 2](/assets/img/Pliers_Iteration2.jpg)

The final iteration reduced the clearance between the spring and handles to 0.05 mm, resulting in a perfect press-fit without wobble. The verticle perimeter thickness of the spring was also increased to 4 layers, limiting the amount of flex to a suitable amount.

![Final Iteration](/assets/img/Pliers_Real_Life.jpg)

- **Relevant Specifications**

  Jaw Thickness: 10 mm

  Effective Jaw Length: 10 mm

  Jaw Separation (resting): 3.8 mm

  Jaw Separation (max.): 20 mm

  Jaw Separation (max., alt. spring config.): 24 mm

![Alternative Spring Configuration](/assets/img/Pliers_Alt_Config.jpg)

{% include gallery caption="Multimaterial Pliers" %}
