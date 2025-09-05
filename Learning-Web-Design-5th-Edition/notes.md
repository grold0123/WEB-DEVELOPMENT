# CHAPTER 1: HTML FOR STRUCTURE
**(HTML OVERVIEW)**
-   get a feel for how markup works
    -   elements
    -   attributes 
-   how browsers interpret HTML documents 
-   how HTML documents are structures 
-   style sheet in action 

## A WEB PAGE
in this chapter we tackle five steps that cover 
the basics of page production:
1.  __Start with content.__ 
    As a starting point, we'll write up raw text content and see what browsers do with it.
2.  __Give the document structure.__
    You'll learn about HTML, element syntax and the elements that set up areas for content and metadata.
3.  __Identify text elements.__
    You'll describe the content using the appropriate text elements and learn about the proper way to use HTML.
4.  __Add an image.__
    By adding an image to the page, you'll learn about attributes and empty elements.
5.  __Change how the text looks with a style sheet.__
    This exercise gives you a taste of formatting content with Cascading Style Sheets.

### STEP 1: START WITH CONTENT 
1.  __Type the home page content.__

        Black Goose Bistro

        The Restaurant 
        The Black Goose Bistro offers casual lunch and dinner fare in a relaxed atmosphere. The menu changes regularly to highlight the freshest local ingredients.

        Catering 
        You have fun. We'll handle the cooking. Black Goose Catering can handle events from snacks for a meetup to elegant corporate fundraisers.

        Location and Hours
        Seekonk, Massachusetts;
        Monday through Thursday 11am to 9pm; Friday and Saturday, 11am to midnight 

2.  __Save as index.html in a folder named bistro.__

3.  __Try opening it in a browser.__

4.  __A continuous line of text and a white background.__

### STEP 2: GIVE THE HTML DOCUMENT STRUCTURE
We have our content saved in an HTML document - now we're ready to start marking it up.

#### The Anatomy of an HTML Element

    opening tag         content             closing tag
        |        (may be text and/or      (starts with a/)
        |        other HTML elements)           |
        |                  |                    |
    <element_name>    Content_here         </element_name>

        example:    <h1>Black Goose Bistro</h1>

-   __Elements__ 
    -   Identified by tags in the text source. 
    -   A tag consists of the element name (usually an abbreviation of a longer descriptive name) within angle brackets(<>). 
    -   The browser knows that any text within brackets is hidden and not displayed in the browser window.
    -   The element name appears in the opening tag (also called start tag) <element_name> and again in the closing tag (end tag) preceded by a slash </element_name>.
    -   The closing tag works something like an 'off' switch for the element.
    -   The tags added around content are referred to as the markup.
    -   Important to note that an element consists of both the content and its markup (the start and end tags).
    -   In HTML, capitalization of element names is not important. So <img>, <IMG>, and <Img> are all the same.

-   __Basic Document Structure__

        1-----------    <!DOCTYPE html>
            +-------    <html>
            |
            |    +---   <head>
            |    |          
            |    |          <meta charset='utf-8'> -------4
            | 3--+          <title>Title here</title> ----5
            |    |
        2-- +    |
            |    +---   </head>
            |
            |    +---   <body>
            |    |
            | 6--+      Page content goes here.
            |    |
            |    +---   </body>
            |
            +-------    </html>

1.  __DOCTYPE__. Identifies the document as written in HTML5.
2.  __HTML element.__ The entire document is contained within an html element. The html element is called the root element because it contains all the elements in the document, and it may not be contained within any other element.
3.  __Head element.__ Contains elements that pertain to the document that are not rendered as part of the content, such as its title, style sheets, scripts, and metadata.
4.  __Meta element.__ Provide document metadata, information about the document. In this case, it specifies the character encoding (a standardized collection of letters, numbers, and symbols).
5.  __Title element.__ A descriptive title.
6.  __Body element.__ Contains everything that we want to show up in the browser window.

### STEP 3: IDENTIFY TEXT ELEMENTS 

#### Mark it Up Semantically 
-   The purpose of HTML is to __add meaning and structure to the content__. It is not intended to describe how the content should look.
-   __Semantic Markup.__ Choose the HTML element that provides the most meaningfull description of the content at hand. 
-   For Example. The most important heading at the beginning of the document should be marked up as an h1.

#### Block and Inline Elements 
-   Heading element and paragraph element start on new lines and do not run together as they did before.
-   By default, headings and paragraphs display as block elements.
-   Each block elements begins on a new line, and some space is also usually added above and below the entire element by default.

#### Default Styles 
-   All browsers have their own built-in style sheets called, __user agent style sheets__  that describe the default rendering of elements.


### STEP 4: ADD AN IMAGE
#### Empty Elements 
-   Elements that are used to provide a simple directive.
-   Example is the image element (img), which tells the browser to get an image file from the server and insert it at that spot in the flow of the text.
-   Another example is line break (br), thematic breaks (hr), 
and elements that provide information about a document but don't affect its displayed content, such as the meta element that we used earlier.

                             <element-name>
        example: the br element inserts a line break
        <p>1005 Gravenstein Highway North<br>Sebastopol, CA 95472</p>

#### Attributes 
-   Instructions that clarify or modify an element.
-   For the img element, the __src__ (source) attribute is required, and __specifies the location (URL) of the image file.__
-   The syntax for an attribute is as follows:

        attributename == 'value'

-   Attributes go after the element name, separated by a space. In non-empty elements, attributes go in the opening tag only:

        <element attributename = 'value'>
        <element attributename = 'value'>content</element>

-   You can also put more than one attribute in an element in any order.

        <element attribute1 = 'value' attribute2 = 'value'>

-   Sample of an img element with its required attributes labeled.

                attribute names and values are separated by an equals sign(=)
                 |
        attribute|              attribute name
        name  |  |     value    |
              |  |      |       |           value
              |  |      |       |           |
        <img src = 'bird.jpg' alt = 'photo of bird'>
              |           |  |  |               |
              +-----------+  |  +---------------+
                    |        |         |
                attribute    |     attribute
                             |
                             + multiple attributes are separated by a space

-   Need to know about attributes:
    -   Attributes go __after element name in the opening tag only__, never in the closing tag.
    -   There may be several attributes applied to an element, __separated in the opening tag__. Their order is not important.
    -   Most attributes take values, which follow an equals sign (=)
    -   Some attribute values are single descriptive words. Often called a __Boolean attribute__ because it describes a feature that is either on or off.
    -   A value might be a number, a word, a string of text, a URL, ora measurement, depending on the purpose of the attribute.
    -   Wrapping attribute values in double quotation marks is a strong convention, but are not required and may be omitted. 
    -   Attribute names and values for each element are defined in HTML specifications; in other words, you can't make up an attribute for an element.
    -   The HTML specification also defines which attributes are required in order for the document to be valid.

