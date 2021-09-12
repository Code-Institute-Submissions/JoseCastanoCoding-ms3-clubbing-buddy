<h1 align="center"><strong>Clubbing Buddy</strong></h1>

<h2>3rd Milestone Project</h2>

[View the live project here](https://git.heroku.com/ms3-clubbing-buddy.git)

<img src="" width="600" height="400" />

Clubbing Buddy is a website aimed to help club-goers, ravers and people with an interest in music festivals and gigs, to find companions to go to such events with. The visitors will be given the options to open an account and have a profile that diplays the events they are planning to attend, as well as being able to see what events other users are going to. Think of how many times you have wanted to go to a gig but had no one to go with, or perhaps your partner or friend/s let you down very short notice? This platform could well be the solution to that last minute problem.

The website has been designed to be responsive, intuitive and accessible on a range of devices, including smartphones, tablets and desktops/laptops.

---

## Table of contents

1. [**User Experience**](#user-experience)
    - [**User stories**](#user-stories)
    - [**Design**](#design)
        - [**Colour Scheme**](#colour-scheme)
        - [**Typography**](#typography)
        - [**Imagery**](#imagery)
    - [**Wireframes**](#wireframes)
    
2. [**Features**](#features)
    - [**Existing features**](#existing-features)
    - [**Features left to implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Testing User Stories**](#testing-user-stories)
    - [**Bugs and some other challenges**](#bugs-and-some-other-challenges)
    - [**Final layout**](#final-layout)

5. [**Deployment**](#deployment)
    - [**GitHub Pages**](#github-pages)
    - [**Forking the GitHub Repository**](#forking-the-github-repository)
    - [**Making a Local Clone**](#making-a-local-clone)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Resources**](#resources)
    - [**Acknowledgements**](#acknowledgements)

---

## User Experience

Clubbing Buddy facilitates users with the ability to create an account and have personal login credentials. Once fully registered, users can submit forms with the corresponding information about the event they have on their radar. Users can have visibility of other users profiles in order to connect with them and, potentially, go to events together.

## User stories

-  ### <h3>First Time Visitor Goals</h3>

    1. As a First Time Visitor, I want to open an account and have my own login credentials.
    2. As a First Time Visitor, I want to submit an event I am planning to attend. 
    3. As a First Time Visitor, I want to get in touch with the real people behind Clubbing Buddy, and ask some questions about the platform.

-  ### <h3>Returning Visitor Goals</h3>

    1. As a Returning Visitor, I would like to check other users profiles and see whether there are any events I could join.
    2. As a Returning Visitor, 
    3. As a Returning Visitor, I would like to keep interacting with the owners of the site, by sending them an enquiry about anything in regards to the information displayed about the trail, location or key characteristics of it.

## Design

- ### <h3>Colour Scheme</h3>

I wanted to keep the design of the website simple and neat. I have applied a hero image to be the main background of the website, please see below:

<img src="assets/images/hero-image.jpg" width="600" height="400" />

I picked a combination of colours that I consider to be eye-catching, and that does not take the attention of the user away from the main goal of the website. 

<img src="assets/images/colours.jpg" width="600" height="400" />

There are 2 dominant colours that can be identified on my site:

- <strong>Black galvanised (rgb(26, 23, 23))</strong> : Used as the background colour for the header, footer and the drop down menus as well as the result box (where the trail is revealed once the user has made their choices).
- <strong>Intense Orange (#ff3b00eb)</strong> : Used as the colour of the text displayed on the header, footer and the drop down menus as well as the result box (where the trail is revealed once the user has made their choices).

- ### <h3>Typography</h3>

The font I used for all the website is "Space Grotesk".

<img src="assets/images/font.PNG" width="1000" height="150" />

- ### <h3>Imagery</h3>

All the images I used for my project can be found in the following [link](assets/images) 

I used the site [Unsplash](https://unsplash.com/) to download all my images, with the exception of the ones corresponding to the mountain bike trails I have based my website on. I acquired those one via facebook groups where I am a member of.

## Wireframes

All the wireframes I drew can be found in the following [link](/workspace/east-sussex-mtb-trails/wireframes)

## Features

The site counts with 1 pages in total, where the user can choose from two

### Existing Features

- It is responsive to screen size thanks to bootstrap and the media queries I have put in place.

- There are 9 possible combinations of user choices from the drop-downs, as per the table below:

    SKILL LEVEL | FITNESS LEVEL | MTB TRAIL
    ----------- | ------------- | ---------
    BEGGINER | AVERAGE | STANMER PARK  
    BEGGINER | FIT | STANMER PARK
    BEGGINER | SUPER FIT! | FRISTON FOREST
    INTERMEDIATE | AVERAGE | STANMER PARK
    INTERMEDIATE | FIT | FRISTON FOREST
    INTERMEDIATE | SUPER FIT! | SURREY HILLS
    ADVANCED | AVERAGE | STANMER PARK
    ADVANCED | FIT | FRISTON FOREST
    ADVANCED | SUPER FIT! | SURREY HILLS

 1.	If the user selects beginner (skills) and average (fitness levels), the mtb trail we recommend is Stanmer Park.
 2. If the user selects beginner (skills) and fit (fitness levels), the mtb trail we recommend is Stanmer Park.
 3. If the user selects beginner (skills) and super fit! (fitness levels), the mtb trail we recommend is Friston Forest.
 4. If the user selects intermediate (skills) and average (fitness levels), the mtb trail we recommend is Stanmer Park.
 5. If the user selects intermediate (skills) and fit (fitness levels), the mtb trail we recommend is Friston Forest.
 6. If the user selects intermediate (skills) and super fit! (fitness levels), the mtb trail we recommend is Surrey Hills.
 7. If the user selects advanced (skills) and average (fitness levels), the mtb trail we recommend is Stanmer Park.
 8. If the user selects advanced (skills) and fit (fitness levels), the mtb trail we recommend is Friston Forest.
 9. If the user selects advanced (skills) and super fit! (fitness levels), the mtb trail we recommend is Surrey Hills.

- RESULTS BASED ON USER CHOSEN OPTIONS

1. If the result is Stanmer Park, the home page will display a picture of Stanmer Park and 3 interactive buttons to show:
    - 1.1 The distance to cover going uphill.
    - 1.2 The distance to cover going downhill.
    - 1.3 Tips about Stanmer Park trails.
- The home page will, also, display a google maps api integration and a contact form, using mailjs api integration to get in touch with us to find out more about the trails at Stanmer Park.

2. If the result is Friston Forest, the home page will display a picture of Friston Forest and 3 interactive buttons to show:
    - 2.1 The distance to cover going uphill.
    - 2.2 The distance to cover going downhill.
    - 2.3 Tips about Friston Forest trails.
- The home page will, also, display a google maps api integration and a contact form, using mailjs api integration to get in touch with us to find out more about the trails at       Friston Forest.

3. If the result is Surrey Hills, the home page will display a picture of Surrey Hills and 3 interactive buttons to show:
    - 2.1 The distance to cover going uphill.
    - 2.2 The distance to cover going downhill.
    - 2.3 Tips about Surrey Hills trails.
- The home page will, also, display a google maps api integration and a contact form, using mailjs api integration to get in touch with us to find out more about the trails at Surrey Hills.

### Features left to implement

- 
  
 ##### back to [contents](#table-of-contents)

---
## Technologies Used

- Languages : HTML, CSS, Bootstrap framework and Javascript.

- IDE: [Gitpod](https://www.gitpod.io/) (runs Visual Studio code online).

- Version control: Git on [Gitpod](https://www.gitpod.io/) and [Github](https://github.com/).

- Wireframes: [Balsamiq](https://balsamiq.com/)

- Browser Developer tools : [Google Chrome](https://www.google.com/chrome)

- Fonts : [Google Fonts](https://fonts.google.com/)

- Icons : [Fontawesome](https://fontawesome.com/)

- Hover effects : [Hover.css](https://ianlunn.github.io/Hover/#effects)

- Colour Picker : [colourpicker](https://www.w3schools.com/colors/colors_picker.asp)

- RGB Generator : [rgbgenerator](https://www.coolgenerator.com/rgb-color-generator)

##### back to [contents](#table-of-contents)  

---
## Testing

 The following tools were utilised to test the website:

 - [Pingdom Website Speed Test](https://tools.pingdom.com/)

 The results of such test can be seen as below:

 <img src="assets/images/readme-images-and-documentation/loadingspeed.PNG" width="400" height="300" />

 - [W3C CSS Validator - Results](https://jigsaw.w3.org/css-validator/validator)
 - [W3C Markup Validator - Results](https://validator.w3.org/nu/#textarea)

 In regards to the HTML markup, I encountered one error that even though it did not affect the functionality of the site, it was marked as non-valid code, see below:

 <img src="assets/images/readme-images-and-documentation/errorhtml.PNG" width="1000" height="300" />

 After trying numerous types of fixes, I eventually managed to cut some code from [Bootstrap navbar documentation](https://getbootstrap.com/docs/5.0/components/dropdowns/) and embedded it onto my existing navbar code I previously extracted from Bootstrap. The problem of a div element being a child of an ul was solved
 by changing the div element by a li, which will perfectly fit as a child of an ul. My original classes and id's were kept as they did not need to change at all.

 You can check my clean, no-errors HTML [here](https://validator.w3.org/nu/#textarea)

 In regards to the CSS, no errors. Please see below: 

 <img src="assets/images/readme-images-and-documentation/cssresults.PNG" width="1000" height="300" />

 - [Responsive Web Design](http://ami.responsivedesign.is/)

 The website has been tested in various devices and I have also used the dev tools to make sure that the site renders adequately on all the breakpoints.

### Testing User Stories

-  ### <h3>First Time Visitor Goals</h3>

    1. As a First Time Visitor, I want to browse through the catalogue of products and make enquiries for items I want to purchase.
        - This has been tested and an user will be more than able to browse through the sections of the shop and select any items, by clicking on the call-to-action buttons to buy the product.
    2. As a First Time Visitor, I want to analyse the site and evaluate how easy it is to navigate throught it in order to check the products and content.
        - Navigation menu works perfectly, and each section has an underline efect to make sure the user sees where he/she goes next. On smaller devices such as smartphones, the menu will toggle and
        still will have all the functionality an user needs.
    3. As a First Time Visitor, I want to verify testimonials about the quality of the service and find out what real people think about the website. I will also corroborate
        all their social media channels by clicking on the social media icons displayed on the site, with the aim of getting a deeper insight of their followings on each of the social
        media platforms they are part of.
        - Testimonials are shown right on the home page, and all the links to social media channels are working accordingly.

-  ### <h3>Returning Visitor Goals</h3>

    1. As a Returning Visitor, I might want to place an order or follow up on an enquiry I recently made.
        - All buttons to buy products are fully working so the user will be more than able to perfom such action.
    2. As a Returning Visitor, I want to check any possible new releases or products available on the website.
        - The website will be updated with new products on a daily basis so users can come back and check the latest releases.
    3. As a Returning Visitor, I want to keep up with any promotions running via the official social media accounts of The Vinyl Aficionado website.
        - Social media channels will always be available for the users just by clicking on the links provided on the site.

### Bugs and some other challenges    

One of the navigation items (shop) tends to come off the alignment with the rest of the items. I managed to apply some padding and center it with the rest of items. However, I have
noticed that, when being in one of the pages of the shop, the item comes off although we are probably talking a quarter of a cm.

The Carousel slider from bootstrap was challenging and I very much enjoyed breaking down the code and implementing a first slide that will be the main sign of identity of my website, visually speaking.

The markup of my HTML showed (as previously mentioned) a piece of non-valid code. I was able to fix the issue by using the following [Bootstrap navbar documents](https://getbootstrap.com/docs/5.0/components/dropdowns/)

### Final layout

 - Home Page: I introduced the carousel slider instead of a static photo, as per my wireframe I drew back when I was starting the project.
 - Shop: I deployed a dropdown menu with all the sections of the shop, rather than displaying them all on a single page.


##### back to [contents](#table-of-contents)

---
## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the GitHub Repository.
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu. 
3. Scroll down the Settings page until you locate the "GitHub Pages" Section. 
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.

### Forking

You may wish to contribute to this website and have your contribution published, if so, you are welcome to follow these steps below.

1. Log in to GitHub and locate the GitHub Repository
2. Open https://josecastanocoding.github.io/the-vinyl-aficionado/ 
3. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
4. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

If you prefer working on the repository locally, you can clone the repository to your desktop by the following steps.

1. Go to [the vinyl aficionado github page](https://josecastanocoding.github.io/the-vinyl-aficionado/)
2. Under the repository name, click "Clone or download".
3. - To clone the repository using HTTPS, under "Clone with HTTPS", click the paste icon. 
   - To clone the repository using an SSH key, click Use SSH, then click the paste icon. 
   - To clone a repository using GitHub CLI, click Use GitHub CLI, then click the paste icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
5. Type 'git clone', then paste the URL you copied earlier above. 
6. Press Enter to create your local clone.

##### back to [contents](#table-of-contents)  

---
## Credits

### Content

- [The Record Bloke](https://therecordbloke.com) 
- [Wasted Heroes](https://www.wastedheroes-shop.com/)

### Resources

- [Code Institute](https://learn.codeinstitute.net/)
- [Typewolf](https://www.typewolf.com/google-fonts)
- [Design Shack](https://designshack.net/articles/trends/best-website-color-schemes/)
- [Unsplash](https://unsplash.com/)
- [Bootstrap components](https://getbootstrap.com/)
- [W3schools](https://www.w3schools.com/)
- [Code institute's Slack workspace channels](https://slack.com)
- [CSS tricks](https://css-tricks.com/) 
- [Stack Overflow](https://stackoverflow.com/)
- [Hover.css](https://ianlunn.github.io/Hover/#effects)
- [CSS Gradient](https://cssgradient.io/gradient-backgrounds/)

### Acknowledgements

- [The Record Bloke](https://therecordbloke.com) 
- [Wasted Heroes](https://www.wastedheroes-shop.com/)
- Various people at the [code institute](https://codeinstitute.net/) and on the code institute Slack channel.
- Various people at [LinkedIn](https://www.linkedin.com/)
- My career consultant Stuart Crang.
- My mentor Aaron.

 ##### back to [contents](#table-of-contents)   



