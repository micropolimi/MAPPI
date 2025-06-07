# Build your own APPI platform

This section presents a step-by-step guide to facilitate the replication of the APPI setup, using the components listed at the following [link].

## Horizontal arm

<img src="https://github.com/micropolimi/APPI/raw/main/images/gif_horizontal_arm_scaled.gif" width="500">

### Step 1: LED, lens and filter units.
#### LED unit
Begin by taking the LED (1) and mounting the (Unknown) component onto it (2). Next, place the [LCP36] on top of the (Unknown) and insert and fix three rods ([ER8-P4], 3). Position the rods to minimize the portion which extends beyond the cage on the LED side. Using three rods instead of four will facilitate the installation of the subsequent components. Finally, mount the iris ([LCP50D]) in such a way that it remains easily accessible once the entire setup is assembled.

<img src="https://github.com/micropolimi/APPI/raw/main/images/LED_unit.png">

#### Lens unit
Take the clamping platform ([XT66C4], 1) and mount the 5 cm post holder on top of it (2). Then add the [...] (3), and finally mount the cage that will hold the lens ([LCP34/M], 4).

<img src="https://github.com/micropolimi/APPI/raw/main/images/lens_unit.png">

#### Filter unit
Take the clamping platform ([XT66C4], 1) and mount the 5 cm post holder on top of it (2). Add the [...] (3), and then mount the cage that will be used to hold the short-pass filter ([LCP33/M], 4). Finally, insert the filter into the [LCP33/M]. No retaining ring is required to secure the filter, as the [SM1A2] adapter will serve this function during the assembly of the entire horizontal arm.

<img src="https://github.com/micropolimi/APPI/raw/main/images/filter_unit.png">

### Step 2: assemble the horizontal arm

Mount the horizontal rail ([XT66SD-500], 1) onto the breadboard. Pay close attention to positioning, ensuring that there is sufficient space on the breadboard to place the sample 45 cm away from the last lens once the entire setup is assembled. Fix the lens unit onto the rail (2). At this stage, the exact position of the lens unit along the rail is not critical. Once the entire illumination unit is complete, it can be precisely positioned along the rail thanks to the movable clamping platforms. Next, add the LED unit (3), followed by the filter unit (4). The LED, lens, and filter units are connected using rods. You can now screw the lens ([AC508-075-A-ML]) onto the lens unit (5). The distance between the iris mounted on the LED unit and the center of the lens must be approximetely 9 cm. As a result, the lens will create an enlarged image of the homogeneous illumination plane formed at the iris, located 45 cm away. The most effective way to correctly adjust the distance between the iris and the lens is to temporarily remove the filter unit from the rail and observe how the illumination plane behaves at a distance of 45 cm from the lens, while adjusting the position of the LED unit relative to the lens unit. The optimal position is the one that maximizes the homogeneity of the illumination at 45 cm. Open and close the iris aperture to ensure that the homogeneity of the illumination plane does not depend on the iris aperture. Mount the [SM2L15] tube onto lens (6).

<img src="https://github.com/micropolimi/APPI/raw/main/images/h_panel_1.png">

Once you are satisfied with the positioning of the LED relative to the lens, you can reattach the filter unit to the rail. The filter unit should be positioned at the focal plane of the lens, where the image of the LED source (four emitters) is formed (see image below). Identify this point along the optical path and fix the filter unit in place.

<img src="https://github.com/micropolimi/APPI/raw/main/images/4_emitters.jpeg">

Add the [SM1A2] to the filter unit (7). This will secure the filter within its cage. Mount the [SM2L20] tube onto the SM1A2 (8). The illumination unit is now complete. You can adjust its position on the rail and place it in its final location.

<img src="https://github.com/micropolimi/APPI/raw/main/images/h_panel_2.png">

Mount the base adapter ([BE1]) and the post holder, and secure them to the breadboard using a clamp (9). Insert the rod (10) and screw the camera onto it (11). You can now connect the camera (12). Mount the objective onto the camera (13), add the 3D-printed support for the filter (14), and then screw in the [SM2L05] tube containing the mounted band-pass filter (15). The horizontal arm of the APPI setup is now complete. 

## Vertical arm

<img src="https://github.com/micropolimi/APPI/raw/main/images/gif_vertical_arm_scaled.gif" width="500">

### Step 1: camera unit

<img src="https://github.com/micropolimi/APPI/raw/main/images/camera_unit.png">

### Step 2: assemble the vertical arm


[link]: https://github.com/micropolimi/APPI/blob/main/docs/components.md
[LCP36]: https://www.thorlabs.de/thorproduct.cfm?partnumber=LCP36
[ER8-P4]: https://www.thorlabs.com/thorproduct.cfm?partnumber=ER8-P4
[LCP50D]: https://www.thorlabs.com/thorproduct.cfm?partnumber=LCP50D
[XT66C4]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66C4
[LCP34/M]: https://www.thorlabs.com/thorproduct.cfm?partnumber=LCP34/M
[LCP33/M]: https://www.thorlabs.com/thorproduct.cfm?partnumber=LCP33/M
[SM1A2]: https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1A2
[XT66SD-500]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66SD-500
[AC508-075-A-ML]: https://www.thorlabs.com/thorproduct.cfm?partnumber=AC508-075-A-ML
[SM2L15]: https://www.thorlabs.com/thorproduct.cfm?partnumber=SM2L15
[SM1A2]: https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1A2
[SM2L20]: https://www.thorlabs.com/thorproduct.cfm?partnumber=SM2L20
[BE1]: https://www.thorlabs.com/thorproduct.cfm?partnumber=BE1/M#ad-image-0
[SM2L05]: https://www.thorlabs.com/thorproduct.cfm?partnumber=SM2L05