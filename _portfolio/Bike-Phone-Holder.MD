---
title: "Bike Phone Holder"
excerpt: "Designed with top-down modeling"
header:
  image: /assets/img/uFluidic_Rendering.png
  teaser: /assets/img/uFluidic_Rendering.png
gallery:
  - image_path: assets/img/uFluidic_Rendering.png
  - image_path: assets/img/uFluidic_Mold.jpg
  - image_path: assets/img/uFluidic_Demolding.jpg
  - image_path: assets/img/uFluidic_Device.jpg
---

## Top-Down Modeling

This project utilizes a top-down modeling approach to design phone holder for a bike or scooter that allows the phone to rotate between portrait and landscape mode. Top-down modeling involves designing multiple components within a single assembly file, as opposed to a more traditional bottom-up approach, where the components ae generated individually and then brought together into a final assembly. Top-down modeling allows new components to easily reference existing dimensions and profile shapes, streamlining the design process. For designing this bike phone holder, the top-down approach was implemented as it greatly simplifies the iteration process, especially when fine-tuning the detent mechanism. Top-down modeling also ensures the consistency of the model when updating component geometries, as all components are designed in relation to each other.

## Design Rationale

Like many of my previous projects, this phone holder pursues a minimalistic design, using the least amount of components to build a sturdy product in the most straightforward fashion. The entire phone consists of only four separate components: a back clamp component, a front clamp component that also serves as the inner detent partner, an outer detent partner component, and a phone holder component. Using the minimal amount of components largely simplifies the design prototyping and post-print assembly process. The clamps are modeled for handlebars with a 22.2 mm diameter. The phone holder is modeled specifically for a Samsung S23+, ensuring a snug fit. The camera matrix is not blocked by the holder component, allowing the user to take photos or record videos en route.

The rotation feature of the phone holder is enabled by a ball detent mechanism. The mechanism involves a steel ball bearing (8 mm diameter) that rests on a compression spring (20 mm length) mounted in the inner detent partner piece. The outer detent partner contains 8 semi-cylindrical grooves for the ball bearing to rest in. The spring is compressed when the outer detent partner is in resting position, and compressed even more when the outer detent partner is rotated. This provides sufficient resistance to rotation, and enough force to lock the outer detent partner in portrait or landscape mode. In the assembled phone holder, this detent mechanism demonstrated outstanding performance, being able to lock the phone in either portrait or landscape mode with almost no wobble, generates a satisfying clicking sound when rotating, and requires just the right amount of force to rotate, which was accomplished by choosing an appropriate groove depth in the outer detent partner.

The front and back clamps were powder printed using SLS with PA 12 Nylon powder. Powder printing generates mechanistically stronger and more isotropic parts compared to filament printing, and was applied to print the two clamp components that would need to resist structural deformation when clamping down on the handlebar. The structure of the front clamp/inner detent partner also rendered it extremely hard to set up for filament printing, making the support-free powder printing the best available option. The outer detent partner was filament printed with PLA, resulting in a lightweight model. Since this component needed to be iterated with various groove depths, filament printing was the fastest prototyping option. Layer delamination typically associated with filament printing was not a concern regarding the outer detent component, as rotation was the only motion involved. To account for the filament printing process and to generate enough clearance for rotation, I introduced a 0.45 mm offset between the inner and outer detent, which turned out perfect in the final assembly. The phone holder component was filament printed with TPU 95A. Parts printed with TPU have a rubbery texture that generate a high amount of friction, making it suitable for holding the phone and preventing it from slipping out of the phone holder. While modeling the phone holder component, the thickness of the phone was offset by 0.7 mm to account for 3D printing inaccuracies and the thickness of the screen protector.

## Assembly Instructions

After printing all components and cleaning powder printed parts, install a M5 heat set insert on the front clamp/inner detent component, and four M3 heat set inserts on the outer detent component. Put the 20 mm spring into the allotted slot in the inner detent component, and the 8 mm ball bearing on top of the spring. Pressing down on the ball bearing, slide the outer detent partner onto the inner detent partner, taking care not to release the press on the ball bearing until it rests safely inside the outer detent's groove. Using a M5 x 8 mm screw, secure the outer detent partner onto the inner detent partner. Keep in mind that this screw should not be tightened all the way and should allow the outer detent component to rotate. Position the phone holder such that the four through holes match the locations of the four pre-installed M3 heat set inserts. Using four M3 x 6 mm screws, tighten the phone holder component onto the outer detent partner. This time tighten the screw all the way so the screw head rests inside the offset slot or it will scratch the backplate of the phone. Position the front and back clamps around the bike/scooter handlebar. Using four M5 x 20 mm screws and four M5 hex nuts, tighten the clamps until the phone holder is securely mounted on the handlebar.


