---
title: "Microfluidic Device"
excerpt: "For the separation of microparticles"
header:
  image: /assets/img/Syringe_Pump_Rendering_2.png
  teaser: /assets/img/Syringe_Pump_Rendering_2.png
gallery:
  - image_path: assets/img/Syringe_Pump_Real_Life_1.jpg
  - image_path: assets/img/Syringe_Pump_Rendering_1.png
  - image_path: assets/img/Syringe_Pump_Rendering_2.png
---

## **Introduction**

### What is a microfluidic device?
A microfluidic device is an innovative miniscule system designed to precisely manipulate small amount of fluids through microscale internal channels. By varying channel geometry, microfluidic devices can perform versatile tasks from mixing fluids and particle sorting to microscale reaction and detection. With its miniature size and precise control of fluid movement, microfluidic devices enable high material throughput with low reagent consumption, and has thus found its way into areas like biomedical & healthcare, biological research and environmental monitoring. This project aims to create a prototype microfluidic device that utilizes *pinched flow fractionation* to efficiently separate microparticles based on size.

### What is pinched flow fractionation?
Pinched flow fractionation (PFF) is a simplistic but efficient design proposed by Yamada and coworkers in 2004 for the sized-base separation of particles suspended in a fluid^1^. The key structure of PFF is a narrow pinch section where fluids with and without particles mix, followed by a broad section where the particles are separated. The two fluids are each introduced to the microfluidic chip through a channel, and directed to the pinch section. By controlling the flow rates of the two fluid streams, the particles are forced to align to one sidewall of the pinch section where the two streams intersect. At the end of the pinch section where the liquid flow starts to broaden, the differential force of the channel sidewall on particles of different sizes causes the particles' trajectory to slightly differentiate. Consequently, this slight positional difference is amplified by the broadening of the fluid in the broad section, effectively positions the particles at different locations in the laminar flow profile. Splitting the stream exiting the broad section based on particle position then allows particles of various sizes to be collected in separate streams.

### What is small particle sorting used for?
Small particle sorting has certainly found its applications in biomedical and healthcare research. To investigate how infectivity profiles of viruses correlate with particle size, Gaudin and coworkers implemented a flow virometry assay and effectively separated Junin virus particles of various sizes while conserving their biological activities. The authors then analyzed the virions of different sizes and determined that larger virus particles are twice as infective as smaller virions. As demonstrated by this paper, size-based sorting is an efficient way for researchers to analyze particles individually to determine how certain properties of particles relate to size.

## **Instructions**

### CAD Model
The mold for this microfludic device was created in Fusion 360 (Autodesk). The mold was designed for the casted device to have a width of 25 mm and a length of 75 mm, allowing the microfluidic chip to sit on a common microscope slide. The inlets and outlets for the device were designed for microfluidic barbs with a 1.5 mm barb diameter and a 11 mm outer diameter. Cylindrical wells with a 4 mm diameter and 3 mm height were added under each inlet and outlet to prevent fluid overflow. A chamfer was added to the edge of the mold for convenient demolding. A 3 mm bonding buffer zone (where no feature is present) was incorporated into the edge of the mold to ensure watertight bonding to the glass slide.  All aspect ratios within the mold were kept under 4:1 to prevent tall structures from breaking during printing, post-processing or demolding.

### Printing the Mold
The mold for the microfluidic device was fabricated using a Form 4 SLA printer (Formlabs) with Clear v5 resin. As the bottom surface of the mold is where the casted device binds to the glass slide, the model was set up in Preform such that the bottom surface is parallel to the resin vat for it to be completely flat. The *z-*axis resolution was set to the minimum value of 0.025 mm in the Preform software, while the resin printer provided a minimum feature size along the *x-* or *y-* axes of 85 microns. The completed print, while still on the build plate, was washed in FormWash filled with isopropyl alcohol (IPA) for 5 minutes. The mold was then removed from the build plate and washed for another 5 minutes in fresh IPA in a stationary bath. The mold was then dried for 30 minutes by leaning it upside down, preventing IPA from pooling inside the device. Any debris present in the mold was dislodged by blowing compressed air onto the mold. The model was then cured under UV light for 60 seconds at room temperature. Extreme care was taken at all post-processing steps to ensure that nothing touched the inner surface of the mold, as surface roughness could disrupt the watertight seal on the final device.

### Parylene Coating
After post-processing, the mold was coated with 2 grams of parylene-C in a Labcoter PDS 2010 parylene deposition machine (Specialty Coating Systems).

### Casting with PDMS
The device was casted with polydimethyl siloxane (PDMS) by pouring a 10:1 weight ratio mixture of PDMS (Sylgard 184, Ellsworth Adhesive Company) and curing agent into the parylene-coated mold. The casted PDMS mixture was then degassed for 30 minutes in a vacuum chamber, and cured in an oven at 80°C for 3 hours.

### Plasma Bonding to Glass Slide
The cured PDMS device was removed from the resin mold, and bonded to a 25 mm by 75 mm glass slide using a PlasmaFlo PDC-FMG plasma cleaner (Harrick Plasma), giving the completed microfluidic device.



