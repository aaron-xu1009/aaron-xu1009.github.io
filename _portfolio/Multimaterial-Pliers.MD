---
title: "Multimaterial Pliers"
excerpt: "Print-in-place pliers for picking up resistors"
header:
  image: /assets/img/uFluidic_Rendering.png
  teaser: /assets/img/uFluidic_Rendering.png
gallery:
  - image_path: assets/img/uFluidic_Rendering.png
  - image_path: assets/img/uFluidic_Mold.jpg
  - image_path: assets/img/uFluidic_Demolding.jpg
  - image_path: assets/img/uFluidic_Device.jpg
---

## **Introduction**

- Introduction

Print-in-place models are multiplecomponent designs that work immediately after printing, requiring no post-printing processing. This is achievable through single material extrusion, but the models have to be carefully designed to allow for motion or rotation. When filament printing, these single material designs would also have to be properly oriented and print settings carefully tuned. Even with these caveats outmaneuvered, single material extrusion still face its limitations due to irregularities of plastic extrusion, and material wearing away or degrading caused by friction. Since filament printing is capable of utilizing different thermoplastics, a potential alternative would be to use multiple materials. A rigid plastic, such as TPU or ABS, could be used to print a part requiring strong mechanical properties, while an elastomer, such as TPU, could be used to print parts involved in motion or where higher friction is required. Commercial 3D printers now offer upgrade kits that allow multiple filaments to be used on the same print bed, allowing a print-in-place model to be created with multiple materials. Real-life applications of multimaterial print-in-place models include 

These can be created through single material extrusion by carefully designing models and orienting the print to allow for clearance between printed joints where motion or rotation is needed. However, even with optimized print settings, these models can be plagued by crunchy movement due to the irregularities of plastic extrusion. Another method to obtain useful motion is to include a flexible element in the model, whether that is a thin piece of a rigid plastic or a second elastomeric material.This project aims to leverage the ability of fused filament fabrication (FFF) being able to print different thermoplastics to create a needle nose plier capable of gripping and picking up through-hole resistors. As FFF 3D printers are capable of printing PLA and TPU filaments, the pliers would consist of rigid handles printed with PLA, and a spring component printed with TPU 95A. For ease of use, the spring component would be designed to return the pliers to the open position whenever not in use.

## **Instructions**

- CAD Model

![uFluidic Model](/assets/img/uFluidic_Rendering.png)

- Interactive CAD Model

<iframe src="https://vanderbilt643.autodesk360.com/shares/public/SH286ddQT78850c0d8a4be490e3ce2235985?mode=embed" width="800" height="600" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>
