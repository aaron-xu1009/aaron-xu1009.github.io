---
title: "Microfluidic Device"
excerpt: "For the size-based separation of microparticles"
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

- What is a microfluidic device?

A microfluidic device is an innovative miniscule system designed to precisely manipulate small amount of fluids through microscale internal channels. By varying channel geometry, microfluidic devices can perform versatile tasks from mixing fluids and particle sorting to microscale reaction and detection. With its miniature size and precise control of fluid movement, microfluidic devices enable high material throughput with low reagent consumption, and has thus found its way into areas like biomedical & healthcare, biological research and environmental monitoring. This project aims to create a prototype microfluidic device that utilizes *pinched flow fractionation* to efficiently separate microparticles based on size. The microfluidic device in this project is specifically designed to separate smaller 0.125-0.150 mm polyethylene beads from larger 0.425-0.500 mm beads suspended in solution.

- What is pinched flow fractionation?

Pinched flow fractionation (PFF) is a simplistic but efficient design proposed by Yamada and coworkers in 2004 for the sized-base separation of particles suspended in a fluid. The key structure of PFF is a narrow pinch section where fluids with and without particles mix, followed by a broad section where the particles are separated. The two fluids are each introduced to the microfluidic chip through a channel, and directed to the pinch section. By controlling the flow rates of the two fluid streams, the particles are forced to align to one sidewall of the pinch section where the two streams intersect. At the end of the pinch section where the liquid flow starts to broaden, the differential force of the channel sidewall on particles of different sizes causes the particles' trajectory to slightly differentiate. Consequently, this slight positional difference is amplified by the broadening of the fluid in the broad section, effectively positions the particles at different locations in the laminar flow profile. Splitting the stream exiting the broad section based on particle position then allows particles of various sizes to be collected in separate streams.

- What is small particle sorting used for?

Small particle sorting has certainly found its applications in biomedical and healthcare research. To investigate how infectivity profiles of viruses correlate with particle size, Gaudin and coworkers implemented a flow virometry assay and effectively separated Junin virus particles of various sizes while conserving their biological activities. The authors then analyzed the virions of different sizes and determined that larger virus particles are twice as infective as smaller virions. As demonstrated by this paper, size-based sorting is an efficient way for researchers to analyze particles individually to determine how certain properties of particles relate to size.

An application of small particle sorting in environmental fields, as described by Gong and coworkers, involves the sorting of marine microplastics with a microfluidic device. Using the microfluidic chip, they were able to isolate microplastics as small as 50 microns, eliminating the need of labeling processes. Raman spectroscopy and machine learning models were then implemented to identify the trapped plastics, which would assist in determining the source of plastic pollutant. This is an excellent exhibit of the effectiveness of microfluidic devices in small particle sorting.

## **Instructions**

- CAD Model

The mold for this microfludic device was created in Fusion 360 (Autodesk). The mold was designed for the casted device to have a width of 25 mm and a length of 75 mm, allowing the microfluidic chip to sit on a common microscope slide. The inlets and outlets for the device were designed for microfluidic barbs with a 1.5 mm barb diameter and a 11 mm outer diameter. Cylindrical wells with a 4 mm diameter and 3 mm height were added under each inlet and outlet to prevent fluid overflow. A chamfer was added to the edge of the mold for convenient demolding. A 3 mm bonding buffer zone (where no feature is present) was incorporated into the edge of the mold to ensure watertight bonding to the glass slide.  All aspect ratios within the mold were kept under 4:1 to prevent tall structures from breaking during printing, post-processing or demolding.

![uFluidic Model](/assets/img/uFluidic_Rendering.png)

- Interactive CAD Model

<iframe src="https://vanderbilt643.autodesk360.com/shares/public/SH286ddQT78850c0d8a48604a9f682a8be85?mode=embed" width="640" height="480" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true"  frameborder="0"></iframe>

- Printing the Mold

The mold for the microfluidic device was fabricated using a Form 4 SLA printer (Formlabs) with Clear v5 resin. As the bottom surface of the mold is where the casted device binds to the glass slide, the model was set up in Preform such that the bottom surface is parallel to the resin vat for it to be printed completely flat. The *z-*axis resolution was set to the minimum value of 0.025 mm in the Preform software, while the resin printer provided a minimum feature size along the *x-* or *y-* axes of 85 microns. The completed print, while still on the build plate, was washed in FormWash filled with isopropyl alcohol (IPA) for 5 minutes. The mold was then removed from the build plate and washed for another 5 minutes in fresh IPA in a stationary bath. The mold was then dried for 30 minutes by leaning it upside down, preventing IPA from pooling inside the device. Any debris present in the mold was dislodged by blowing compressed air onto the mold. The model was then cured under UV light for 60 seconds at room temperature. 

*Extreme care was taken at all post-processing steps to ensure that nothing touched the inner surface of the mold, as surface roughness could disrupt the watertight seal on the final device.*

![uFluidic Mold](/assets/img/uFluidic_Mold.jpg)

- Parylene Coating

After post-processing, the mold was coated with 2 grams of parylene-C in a Labcoter PDS 2010 parylene deposition machine (Specialty Coating Systems).

- Casting with PDMS

The device was casted with polydimethyl siloxane (PDMS) by pouring a 10:1 weight ratio mixture of PDMS (Sylgard 184, Ellsworth Adhesive Company) and curing agent into the parylene-coated mold. The casted PDMS mixture was then degassed for 30 minutes in a vacuum chamber, and cured in an oven at 80°C for 3 hours.

![uFluidic Demolding](/assets/img/uFluidic_Demolding.jpg)

- Plasma Bonding to Glass Slide

The cured PDMS device was removed from the resin mold, and bonded to a 25 mm by 75 mm glass slide using a PlasmaFlo PDC-FMG plasma cleaner (Harrick Plasma), giving the final microfluidic device.

![uFluidic Device](/assets/img/uFluidic_Device.jpg)

- Testing the Device

The microfluidic device was tested through the separation of 2 sizes of polyethylene beads suspended in a Tween solution. The smaller orange beads have diameters ranging from 0.125 to 0.150 mm, and the larger purple beads have diameters ranging from 0.425 to 0.500 mm. The device demonstrated effective separation of the particles.

## Discussion

- The resin-printed mold was coated with parylene before casting with PDMS to generate a thin hydrophobic layer on the mold. This hydrophobic layer creates a non-stick surface on the mold, allowing for smooth demolding of the casted PDMS device. Without the parylene coating, uncured resin in the mold can leach to the bottom surface where PDMS comes into contact with the mold, and interfere with the the crosslinking of PDMS during curing, leading to undesired loss of channel features or incomplete curing.
- Hypothetical applications of this microfluidic device include the size separation of microplastics in seawater, which would allow for an efficient determination of size distribution of plastic pollutants, providing insight into pollution levels. It could also be used for disease detection through the separation of circulating tumor cells from regular blood cells, providing an early detection of cancer or other diseases using perhaps only one drop of blood.
- The microfluidic device was designed using a modified version of the particle distribution equation proposed by Yamada and coworkers in 2004, **%h = (Wp-0.5D)/Wp**, where **Wp** is the width of the pinch section, and **D** is the diameter of the particle of concern. This equation gives **%h** as the percentage height of the particle relative to the broad section width. The device in this project utilizes a pinch section width of 0.625 mm and a broad section width of 17.200 mm. Utilizing the equation gives the particle %h distribution in the following table. The microfludic device designed in this project has the broad section divided into four channels of equal width, meaning that there are three channel barriers at percentage heights of 25%, 50% and 75%. This design effectively separates the small particle from the large particle, as the 75% barrier is between their percentage heights once they reach the broad section. Following a laminar flow profile, the small particle is directed to the uppermost channel, whereas the larger particle is directed to the second highest channel.

| Particle Category | Size | Percentage Height |
| --- | --- | --- |
| Small | 0.125 mm | 90% |
| Small | 0.150 mm | 88% |
| **Channel Barrier** | N/A | **75%** |
| Large | 0.425 mm | 66% |
| Large | 0.500 mm | 60% |

- As mentioned above, the broad section is divided into 4 channels of equal width. The barriers between the channels are designed to be 0.400 mm wide, restricted by the aspect ratio limit. Thin barriers would reduce eddies and turbulent flow near the barriers, which are both detrimental to particle separation. Each of the four channel directs fluid to one of the four outlets without any narrowing or bends, which would eliminate any head loss due to complex geometries. The only difference between flow resistance through the four channels would be caused by wall roughness along different channel lengths, which is limited by the barb's outer diameter. In an ideal situation where the channel walls are perfectly smooth, each of the four outlets would receive an equal 25% of the total inlet flow, and the fluid would follow a perfectly laminar flow profile throughout the device.
- Based on the results of the testing, which showed a slight preference of fluid flow through the shortest channel, changes can be implemented to this device by narrowing the shorter channels and widening the longer channels. Alternatively, if tubing can be directly connected to channel outlets without using barbs, the four outlet channels can be designed to be of equal length, so that the fluid would experience equal amounts of resistance through each channel, reducing the extent of uneven flow rates.

## References
1.	Yamada, M., Nakashima, M. & Seki, M. Pinched Flow Fractionation:  Continuous Size Separation of Particles Utilizing a Laminar Flow Profile in a Pinched Microchannel. Anal. Chem. 76, 5465–5471 (2004).
2.	Gaudin, R. & Barteneva, N. S. Sorting of small infectious virus particles by flow virometry reveals distinct infectivity profiles. Nat. Commun. 6, 6022 (2015).
3.  Gong, L. et al. A microfluidic approach for label-free identification of small-sized microplastics in seawater. Sci. Rep. 13, 11011 (2023).
4.	O’Grady, B. J. et al. Rapid prototyping of cell culture microdevices using parylene-coated 3D prints. Lab. Chip 21, 4814–4822 (2021).
5.	Venzac, B. et al. PDMS Curing Inhibition on 3D-Printed Molds: Why? Also, How to Avoid It? Anal. Chem. 93, 7180–7187 (2021).
