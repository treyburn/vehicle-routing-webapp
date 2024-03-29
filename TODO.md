## TODO
### Required for POC
1. Implement debug mode
    - [x] a. Implement function to generate random distance matrices in place of the API (I ain't made of money...)
    - [ ] b. Implement JSON element for 'debug' in order to bypass the Distance Matrix API
    - [ ] c. Need to implement a timeout for finding the solution (1 minute?)
    - [ ] d. Need to implement a timeout for Distance Matrix API call (10 seconds?)

2. Implement Unit Tests
    - [ ] a. All main() functions in unimplemented_code need unit tests before converting to Flask Models/Resources
    - [ ] b. Need to design a unit test factory class for Flask Models/Resources
    - [ ] c. Implement unit tests for all Flask Models/Resources
    - [ ] d. Implement unit tests for App

3. Implement VRP backend in Flask
    - [ ] a. Create a function to return results as a 'csv' for end user
    - [ ] b. Create a simple sqlite database
        - [ ] i. Store uuid for each POST received
        - [ ] ii. Store the outputs of the model (original inputs + order indication)
        - [ ] iii. Status (Ready / Not Yet Ready / Failed)
        - [ ] iv. May want to future proof and just start off with a user id that will later tie to Login functionality
    - [ ] b. Define required web routes for MVP
        - [ ] i. '/' (Home/splash page - marketing BS for now)
        - [ ] ii. '/Route' (POST - user sends data, and flask returns a random/unique uuid for GET page. GET - returns csv to user)
            - [ ] A. For the GET - need to first check status based on uuid
        - [ ] iii. '/About' - static page
        - [ ] iv. '/Contact' - contact form submission - dump into a SQLite file for now
    - [ ] c. Implement unimplemented_code in the model and resources for VRP

4. Implement bare bones front end
    - [ ] a. Simple landing page
    - [ ] b. Route page
        - [ ] i. CSV upload button
        - [ ] ii. submit button (and push user csv to server)
            - [ ] A. Need to determine if we push a literal csv file or a pure json element with the data (JS would be required)
            - [ ] B. Is there a way to determine if it was successfully uploaded or not? Need to research
        - [ ] iii. Loading widget - for now we might make it a static 5-10 seconds. Real implementation can use react events
        - [ ] iv. Get results button
            - [ ] A. Web page will hold the uuid as a variable - then attach to JSON payload with GET
            - [ ] B. If Status is 'Ready' - it will prompt user for download location and then download results file
            - [ ] C. If status is 'Failed' - then we need an error message of some kind
            - [ ] D. If status is 'Not Yet Ready' - then give the user an indication that their data is still processing
    - [ ] c. About page
        - [ ] i. About me and my professional experience in the geospatial world
    - [ ] d. Contact page
        - [ ] i. Simple contact form - dump to sqlite table for now
    - [ ] c. Basic CSS styling
        - [ ] i. navbar
        - [ ] ii. splash page
        - [ ] iii. nice buttons
        - [ ] iv. nice looking loading widget
##
### Required for MVP
1. Implement basic login functionality
    - [ ] a. Hide route api access behind login
    - [ ] b. Utilize JWT and cookies
    - [ ] c. Implement 'Get previous results' tab in user profile

2. Implement a 'Demo' tab
    - [ ] a. Needs to utilize a known distance matrix table (or segments of one) but appear random
    - [ ] b. Needs to bypass the Distance Matrix API or I will go bankrupt

3. Implement memo-izing of the user's data
    - [ ] a. We don't want to generate a new Distance Matrix (cost/time) if we don't have to
    - [ ] b. Maybe we memoize by an entire csv first (so sort the csv records first then create a unique hash to write to the database)
        - [ ] i. In a later phase we can hash individual segment results too and send less elements to the API (this is probably a major undertaking)
        - [ ] ii. First we sort, then we hash, then we check for matching hash. If matching hash is found we just return the uuid for the GET results associated with it

4. Expose additional model features to the user
    - [ ] a. Number of vehicles
    - [ ] b. Slack time
    - [ ] c. Max distance/time
    - [ ] d. Depot location
    - [ ] e. Choice to optimize by time (incl slack time) or distance
    - [ ] f. Maybe even expose model type? (maybe an advanced tab)

5. UI/UX overhaul
    - [ ] a. Because I'm sure my original UI will be garbage

6. Explore Distance Matrix API alternatives
    - [ ] a. Mapbox
    - [ ] b. Here
    - [ ] c. OSRM
##
### Phase 1 Ideas
1. Implement Capacity Constrained Vehicle Routing (Vehicles can only hold so much cargo) (Check out: Penalties and Dropping Visits)

2. Implement Pickups and Deliveries Options (Like a food delivery service optimization)

3. Implement Time Window Constraints (Must deliver by certain time windows)

4. Implement Resource Constraints (loading/unloading coordination with set number of loading bays)

5. Need way better outputs - maps (especially with route(s) rendered), better file types, turn by turn directions, etc
##
### Phase 2 Ideas
1. Rip out Distance Matrix and replace with an in house solution
    1. Check out OSRM: http://project-osrm.org/
    2. Open source routing engine in C++ which consumes OSM data
    3. Can utilize C++ bindings in python to leverage this

2. Fork OSRM and edit to allow disabling of right/left turns - this will be a *huge* feature 