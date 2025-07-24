# Build your own MAPPI platform
<p align="justify">
This section presents a step-by-step guide to facilitate the replication of the MAPPI setup, using the components listed at the following [link].

## Horizontal arm

<img src="https://github.com/micropolimi/APPI/raw/main/images/gif_horizontal_arm_scaled.gif" width="500">

### Step 1: LED, lens and filter units.
#### LED unit
<p align="justify">
Begin by taking the LED (1) and mounting the [SM2L05] component onto it (2). Next, place the [LCP36] on top of the [SM2L05] and insert and fix three rods ([ER8-P4], 3). Position the rods to minimize the portion which extends beyond the cage on the LED side. Using three rods instead of four will facilitate the installation of the subsequent components. Finally, mount the iris ([LCP50D]) in such a way that it remains easily accessible once the entire setup is assembled (4).

<img src="https://github.com/micropolimi/APPI/raw/main/images/LED_unit.png">

#### Lens unit
<p align="justify">
Take the clamping platform ([XT66C4], 1) and mount the [post holder] on top of it (2). Then add the [post] (3), and finally mount the cage that will hold the lens ([LCP34/M], 4).

<img src="https://github.com/micropolimi/APPI/raw/main/images/lens_unit.png">

#### Filter unit
<p align="justify">
Take the clamping platform ([XT66C4], 1) and mount the [post holder] on top of it (2). Add the [post] (3), and then mount the cage that will be used to hold the short-pass filter ([LCP33/M], 4). Screw a [retaining ring] into the cage and insert the filter into the cage (5). A second retaining ring is not required to secure the filter, as the [SM1A2] adapter will serve this function during the assembly of the entire horizontal arm.

<img src="https://github.com/micropolimi/APPI/raw/main/images/filter_unit.png">

### Step 2: assemble the horizontal arm
<p align="justify">
Mount the horizontal rail ([XT66SD-500], 1) onto the breadboard. Pay close attention to positioning, ensuring that there is sufficient space on the breadboard to place the sample 45 cm away from the last lens once the entire setup is assembled. Fix the lens unit onto the rail (2). At this stage, the exact position of the lens unit along the rail is not critical. Once the entire illumination unit is complete, it can be precisely positioned along the rail thanks to the movable clamping platforms. Next, add the LED unit (3), followed by the filter unit (4). The LED, lens, and filter units are connected using rods. You can now screw the lens ([AC508-075-A-ML]) onto the lens unit (5). The distance between the iris mounted on the LED unit and the center of the lens must be approximetely 9 cm. As a result, the lens will create an enlarged image of the homogeneous illumination plane formed at the iris, located 45 cm away. The most effective way to adjust the distance between the iris and the lens is to temporarily remove the filter unit from the rail and observe how the illumination plane behaves at a distance of 45 cm from the lens, while adjusting the position of the LED unit relative to the lens unit. The optimal position is the one that maximizes the homogeneity of the illumination at 45 cm. Open and close the iris aperture to ensure that the homogeneity of the illumination plane does not depend on the iris aperture. Mount the [SM2L15] tube onto lens (6).

<img src="https://github.com/micropolimi/APPI/raw/main/images/h_panel_1.png">

<p align="justify">
Once you are satisfied with the positioning of the LED relative to the lens, you can reattach the filter unit to the rail. The filter unit should be positioned at the focal plane of the lens, where the image of the LED source (four emitters) is formed (see image below). Identify this point along the optical path and fix the filter unit in place.

<img src="https://github.com/micropolimi/APPI/raw/main/images/4_emitters.jpeg" width="300">

<p align="justify">
Add the [SM1A2] to the filter unit (7). This will secure the filter within its cage. Mount the [SM2L20] tube onto the SM1A2 (8). The illumination unit is now complete. You can adjust its position on the rail and place it in its final location.

<img src="https://github.com/micropolimi/APPI/raw/main/images/h_panel_2.png">

<p align="justify">
Mount the post holder onto the base adapter ([BE1]), and secure them to the breadboard using a [clamping fork] (9). Insert the [post] (10) and screw the camera onto it (11). You can now connect the camera. Mount the objective onto the camera (12), add the 3D-printed support for the filter (13), and then screw in the [SM2L05] tube containing the mounted band-pass filter (14). The horizontal arm of the MAPPI setup is now complete. 

<img src="https://github.com/micropolimi/APPI/raw/main/images/h_panel_3.png">

## Vertical arm

<img src="https://github.com/micropolimi/APPI/raw/main/images/gif_vertical_arm_scaled.gif" width="500">

### Step 1: camera and illumination units
#### Camera unit
<p align="justify">
For the vertical arm, the camera must be mounted on a clamping platform ([XT66C4]). Even when using the shortest screw, it is not possible to secure the camera directly to the platform because the threaded hole on the camera is too shallow. To resolve this, two metal rings (available [here]) should be used to increase the effective thickness, as shown in panel 1. Align the rings with the hole on the camera (2), then attach the camera to the clamping platform (3). You're camera unit is ready. Any other strategy to increase the thickness and fix the camera to the platform can be used. 

<img src="https://github.com/micropolimi/APPI/raw/main/images/camera_unit.png">

#### Illumination unit
<p align="justify">
The same instructions used to build the horizontal illumination unit should be followed to assemble the vertical one. The only difference lies in how the lens unit is mounted onto the clamping platform. In this case, the lens unit is secured to the clamping platform using a clamping fork (see figure below). This configuration allows the vertical illumination unit to be slightly tilted rather than perfectly vertical. In this way, it is possible to illuminate the same area imaged by the camera while keeping the camera parallel to the sample plane.

<img src="https://github.com/micropolimi/APPI/raw/main/images/clamp_detail.jpg" width="300">

### Step 2: assemble the vertical arm
<p align="justify">
Mount the vertical shaft ([XT66-100]) using the vertical mounting plate ([XT66P1]), and cover the lower part of the shaft with a black cloth to avoid unwanted light reflections during measurements (1). Mount the illumination unit on one side of the shaft using the clamping platforms (2). Adjust the height of the illumination unit along the shaft according to the sample dimensions, maintaining a distance of 45 cm between the last lens and the sample.
Mount one of the two double dovetail clamps ([XT66C2]) on another side of the shaft (3), specifically on the side where the horizontal arm of the MAPPI platform is located. Attach the cross bracket ([XT66CB]) to the double dovetail clamp (4), then mount the second XT66C2 onto the cross bracket (5). Add the rail ([XT66DP-500]) that will hold the camera vertically above the sample (6). Mount the camera unit onto this rail near the LED (7). Finally, screw the objective (already fitted with the filter) onto the camera, and connect the camera (8). Your MAPPI platform is now complete.

<img src="https://github.com/micropolimi/APPI/raw/main/images/v_panel.png">

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
[XT66-100]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66-100
[XT66P1]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66P1
[XT66C2]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66C2
[XT66CB]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66CB
[XT66DP-500]: https://www.thorlabs.com/thorproduct.cfm?partnumber=XT66DP-500
[post]: https://www.thorlabs.com/thorproduct.cfm?partnumber=TR75/M
[post holder]: https://www.thorlabs.com/thorproduct.cfm?partnumber=PH75/M-P5#ad-image-0
[retaining ring]:https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1RR
[clamping Fork]:https://www.thorlabs.com/thorproduct.cfm?partnumber=CF125C/M#ad-image-0
[here]:https://www.thorlabs.com/thorproduct.cfm?partnumber=HW-KIT2/M