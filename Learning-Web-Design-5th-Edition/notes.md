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

### STEP 5: CHANGE THE LOOK WITH A STYLE SHEET

#### Adding a style sheet

1.  In index.html

2.  The style element is placed inside the document head.
    Start by adding the style element to the document as shown here:

        <head>
            <meta charset='utf-8'>
            <title>Black Goose Bistro</title>
            <style>
            </style>
        </head>

3.  Next, type the following style rules within the style element.

        <style>
        body{
            background-color: #faf2e4;
            margin: 0 10%;
            font-family: sans-serif;
        }
        h1{
            text-align: center;
            font-family: serif;
            font-weight: normal;
            text-transform: uppercase;
            border-bottom: 1px solid #57b1dc;
            margin-top: 30px;
        }
        h2{
            color: #d1633c;
            font-size: 1em;
        }
        </style>


## VALIDATING YOUR DOCUMENTS 

-   __Check your markup yourself.__ Make sure that you have abided by all the rules of whatever version of HTML you are using.

-   __Use a validator.__ 
    Using a web-based validator 
            
            html5.validator.nu
            https://validator.w3.org/


# CHAPTER 2: MARKING UP TEXT

-   A semantically marked-up document ensures your content is available and accessible in the widest range of browsing environments, from desktop computers and mobile devices to assistive screen readers.

-   It also allows non-human readers, such as search engine indexing programs, to correctly parse your content and make decisions about the relative importance of elements on the page.

## PARAGRAPHS            

-   Paragraphs are the most rudimentary elements of a text document.

-   Indicate a paragraph with the p element by inserting an opening 
    (p) tag at the beginning of the paragraph and a closing (\p) tag after it, as shown in this example:

        <p>...</p>
        Paragraph element

        <p>
        Serif typefaces have small slabs at the ends of 
        letter strokes. In general, serif fonts can make 
        large amounts of text easier to read.
        </p> 

        <p>
        Sans-serif fonts do not have serif slabs; their strokes
        are square on the end. Helvetica and Arial are examples of 
        sans-serif fonts. In general, sans-serif fonts appear sleeker
        and more modern.
        </p>

<p>...</p>
Paragraph element

<p>
Serif typefaces have small slabs at the ends of 
letter strokes. In general, serif fonts can make 
large amounts of text easier to read.
</p> 

<p>
Sans-serif fonts do not have serif slabs; their strokes
are square on the end. Helvetica and Arial are examples of 
sans-serif fonts. In general, sans-serif fonts appear sleeker
and more modern.
</p>


-   Visual browsers nearly always display paragraphs on new lines with a bit of space between by default.

-   Paragraph may contain __text, images, and other inline elements (called phrasing content).__

-   Paragraph may __not__ contain __headings, lists, sectioning elements, or any elements that typically display as blocks by default.__

## HEADINGS

-   When you add headings to content, the browser uses them to create a document outline for the page.

-   There six levels of headings, from __h1 to h6.__

-   Assistive reading devices uses the document outline to help users quickly scan and navigate through a page.

-   Search engines also look at heading levels as part of their algorithms __(information in higher reading levels may be given more weight).__

-   It is best practice to start with the Level 1 heading (h1) and work down in numerical order, creating a logical document structure and outline.

        This example shows the markup for four heading levels. Additional heading levels would be marked up in a similar manner.

        <h1>Type Design</h1>
        <h2>Serif Typefaces</h2>
        <p>Serif typefaces have small slabs at the ends of letter strokes. In general, serif fonts can make large amounts of text easier to read.</p>
        <h3>Baskerville</h3>
        <h4>History</h4>
        <p>The history of the Baskervile typeface.</p>
        <h3>Georgia</h3>
        <p>Description and history of the Georgia typeface.</p>
        <h2>Sans-serif Typefaces</h2>
        <p>Sans-serif typefaces do not have slabs at the ends of strokes.</p>

<h1>Type Design</h1>
<h2>Serif Typefaces</h2>
<p>Serif typefaces have small slabs at the ends of letter strokes. In general, serif fonts can make large amounts of text easier to read.</p>
<h3>Baskerville</h3>
<h4>History</h4>
<p>The history of the Baskervile typeface.</p>
<h3>Georgia</h3>
<p>Description and history of the Georgia typeface.</p>
<h2>Sans-serif Typefaces</h2>
<p>Sans-serif typefaces do not have slabs at the ends of strokes.</p>


-   The markup in the example above would create the following document outline:

        1.  Type Design

            1.  Serif Typefaces
                +   text paragraph

                1.  Baskerville

                    1.  Description
                        +   text paragraph
                    
                    2.  History
                        +   text paragraph
                
                2.  Georgia
                    +   text paragraph 

            2.  Sans-serif Typefaces
                +   text paragraph

## THEMATIC BREAKS (HORIZONTAL RULE)

-   If you want to indicate that one topic has completed and another one is beginning, you can insert what the spec calls a 'paragraph-level thematic break' with the __hr__ element.

-   The hr element adds a logical divider between sections of a page or paragraphs without introducing a new heading level.

-   hr is an empty element - you just drop it into place where you want the thematic break to occur , as shown in this example :

        <h3>Times</h3>
        <p>Description and history of the Times typeface.</p>
        <hr>
        <h3>Georgia</h3>
        <p>Description and history of the Georgia typeface.</p>

<h3>Times</h3>
<p>Description and history of the Times typeface.</p>
<hr>
<h3>Georgia</h3>
<p>Description and history of the Georgia typeface.</p>


## LISTS 

-   All list elements -- the lists themselves and the items that go in them -- are displayed as block elements by default, which means that they start on a new line and have some space above and below, but that may be altered with CSS. 

-   Three types of lists:

    -   __Unordered lists.__ Collection of items that appear in no particular order

    -   __Ordered lists.__ Lists in which the sequence of the items is important

    -   __Description lists.__ Lists that consist of name and value pairs, including but not limited to terms and definitions


### Unordered Lists

-   Just about any list of examples, names, componenets, thoughts, or options qualifies as an unordered list.

-   By default, unordered lists display with a bullet before each list item, but you can change that with a style sheet

-   To identify an unordered list, mark it up as a ul element.

-   The opening (ul) tag goes before the first list item, and the closing tag (/ul)  goes after the last item.

-   Then, to mark up each item in the list as a list item use the opening tag (li) and closing tag (/li)

        <ul>
            <li>Serif</li>
            <li>Sans-serif</li>
            <li>Script</li>
            <li>Display</li>
            <li>Dingbats</li>
        </ul>

<ul>
    <li>Serif</li>
    <li>Sans-serif</li>
    <li>Script</li>
    <li>Display</li>
    <li>Dingbats</li>
</ul>



### Ordered Lists 

-   For items that occur in a particular order, such as step instructions or driving directions. 

-   Ordered lists are defined with the ol element

-   The opening tag li and closing tag /li is still used for each item in the list

-   Instead of bullets, the browser automatically inserts numbers before ordered list items.

        <ol>
            <li>Gutenberg develops moveable type (1450s)</li>
            <li>Linotype is introduced (1890s)</li>
            <li>Photocomposition catches on (1950s)</li>
            <li>Type goes digital (1980s)</li>
        </ol>

<ol>
    <li>Gutenberg develops moveable type (1450s)</li>
    <li>Linotype is introduced (1890s)</li>
    <li>Photocomposition catches on (1950s)</li>
    <li>Type goes digital (1980s)</li>
</ol>

-   If you want a numbered list to start at a number other than 1, you can use the start attribute in the ol element to specify another starting number 

        <ol start='16'>
            <li>Highlight the text with the text tool.</li>
            <li>Select the Character tab.</li>
            <li>Choose a typeface from the pop-up menu.</li>
        </ol>

<ol start='16'>
    <li>Highlight the text with the text tool.</li>
    <li>Select the Character tab.</li>
    <li>Choose a typeface from the pop-up menu.</li>
</ol>

### Description Lists 

-   Used for any type of name/value pairs, such as terms and their definitions, questions and answers, or other types of terms and their associated information.

        <dl>...</dl>
        A decription list

        <dt>...</dt>
        A name, such as a term or label

        <dd>...</dd>
        A value, such as a description or definition

<dl>...</dl>
A decription list

<dt>...</dt>
A name, such as a term or label

<dd>...</dd>
A value, such as a description or definition

-   Example 

        <dl>

            <dt>
                Linotype
            </dt>
            <dd>
                <p>
                    Line-casting allowed type to be selected, used, 
                    then recirculated into the machine automatically. 
                    This advance increased the speed of typesetting 
                    and printing dramatically.
                </p>
            </dd>

            <dt>
                Photocomposition
            </dt>
            <dd>
                <p>
                    Typefaces are stored on film then projected onto photo-sensitive 
                    paper. Lenses adjust the size of the type.
                </p>
            </dd>

            <dt>
                Digital type
            </dt>
            <dd>
                <p>
                    Digital typefaces store the outline of the 
                    font shape in a format such as Postscript. 
                    The outline may be scaled to any size for output.
                </p>
                <p>
                    Postscript emerged as a standard due to its 
                    support of graphics and its early support on 
                    the Macintosh computer and Apple laser printer.
                </p>
            </dd>
        </dl>

<dl>

<dt>
    Linotype
</dt>
<dd>
    <p>
        Line-casting allowed type to be selected, used, 
        then recirculated into the machine automatically. 
        This advance increased the speed of typesetting 
        and printing dramatically.
    </p>
</dd>

<dt>
    Photocomposition
</dt>
<dd>
    <p>
        Typefaces are stored on film then projected onto photo-sensitive 
        paper. Lenses adjust the size of the type.
    </p>
</dd>

<dt>
    Digital type
</dt>
<dd>
    <p>
        Digital typefaces store the outline of the 
        font shape in a format such as Postscript. 
        The outline may be scaled to any size for output.
    </p>
    <p>
        Postscript emerged as a standard due to its 
        support of graphics and its early support on 
        the Macintosh computer and Apple laser printer.
    </p>
</dd>
</dl>

-   It is permitted to have multiple definitions with one term and vice versa.

        <dl>
            <dt>
                Serif examples
            </dt>
                <dd>
                    Baskerville
                </dd>
                <dd>
                    Goudy
                </dd>
            
            <dt>
                Sans-serif examples 
            </dt>
                <dd>
                    Helvetica
                </dd>
                <dd>
                    Futura
                </dd>
                <dd>
                    Avenir
                </dd>
        </dl>

<dl>
<dt>
    Serif examples
</dt>
    <dd>
        Baskerville
    </dd>
    <dd>
        Goudy
    </dd>

<dt>
    Sans-serif examples 
</dt>
    <dd>
        Helvetica
    </dd>
    <dd>
        Futura
    </dd>
    <dd>
        Avenir
    </dd>
</dl>

## MORE CONTENT ELEMENTS 

1.   long quotations (blockquote)

2.   preformatted text (pre) 

3.   figures (figure and figcation)

-   These elements are considered __grouping content__ in the HTML5 spec

-   These elements are also displayed by the browser as a block by default.

### Long Quotations 

-   Used in :
    -   Long quotation 
    -   a testimonial 
    -   a sectiona of copy from another source 

-   uses the blockquote element

-   It is recommended that content within blockquote elements be contained in other elements, such as: 
    -   paragraphs
    -   headings
    -   lists

-   Example 

        <p>
            Renowned type designer, Matthew Carter, has this 
            to say about his profession:
        </p>

        <blockquote>
            <p>
                Our alphabet hasn't changed in eons; there isn't 
                much latitude in what a designer can do with the 
                individual letters.
            </p>
            <p>
                Much like a piece of classical music, the score 
                is written down. It's not something that is tampered 
                with, and yet, each conductor interprets that score 
                differently. There is tension in the interpretation.
            </p>
        </blockquote>

<p>
    Renowned type designer, Matthew Carter, has this 
    to say about his profession:
</p>

<blockquote>
    <p>
        Our alphabet hasn't changed in eons; there isn't 
        much latitude in what a designer can do with the 
        individual letters.
    </p>
    <p>
        Much like a piece of classical music, the score 
        is written down. It's not something that is tampered 
        with, and yet, each conductor interprets that score 
        differently. There is tension in the interpretation.
    </p>
</blockquote>

### Preformatted Text

-   For content in which whitespace is important for conveying meaning

-   Use the preformatted text (pre) element

-   It is a unique element in which it is displayed exactly as it is typed
, including all the carriage returns and multiple character spaces.

-   By default, preformatted text is also displayed in a constant-width font __(one in which all the characters are the same width, also called monospace),__ such as Courier.

-   Example 

        <pre>
        This is                     an              example of 
                    text with a         lot of 
                                curious
                                whitespace.
        </pre>
        <p>
        This is         an          example of 
                text with a         lot of      
                                    curious
                                    whitespace.
        </p>

<pre>
This is                     an              example of 
            text with a         lot of 
                        curious
                        whitespace.
</pre>
<p>
This is         an          example of 
        text with a         lot of      
                            curious
                            whitespace.
</p>

### Figures 

-   Identifies content that illustrates or supports some point in the text.

-   A figure may contain:
    -   image
    -   video 
    -   code snippet
    -   text 
    -   or even a table

-   Content in a figure element should be treated and referenced as a self-contained unit.

-   That means if a figure is removed from its original placement in the main flow, both the figure and the main flow should continue to make sense.

        <figure>
        <img src="piechart.png" alt="chart showing fonts on mobile devices">
        </figure>

        <figure>
            <pre>
                <code>
                    body {
                        background-color: #000;
                        color: red;
                    }
                </code>
            </pre>
            <figcaption>Sample CSS rule.</figcaption>
        </figure>


<figure>
<img src="piechart.png" alt="chart showing fonts on mobile devices">
</figure>

<figure>
    <pre>
        <code>
            body {
                background-color: #000;
                color: red;
            }
        </code>
    </pre>
    <figcaption>Sample CSS rule.</figcaption>
</figure>

## ORGANIZING PAGE CONTENT 

-   HTML5 introduced new elements that give semantic meaning to sections of a typical web page or application

    1.  main content __(main)__

    2.  headers __(header)__

    3.  footers __(footer)__

    4.  sections __(section)__

    5.  articles __(article)__

    6.  navigation __(nav)__

    7.  complementary content __(aside)__

### Main Content 

-   Web pages these days are loaded with different types of content.

-   It is helpful to cut to the chase and explicitly point out the main content on the page.

-   Use the main element to identify the primary content of a page or application.

-   The content of a __main __ element should be unique to that page.

        <body>
            <header>
                <main>
                    <h1>
                        Humanis Sans Serif
                    </h1>
                    <!--code continues-->
                </main>
            </header>
        </body>

<body>
    <header>
        <main>
            <h1>
                Humanis Sans Serif
            </h1>
            <!--code continues-->
        </main>
    </header>
</body>

-   The W3C HTML5 specification states that: 

    1.  Pages should have only one main section.

    2.  It should not be nested within an: 
        -   article 
        -   aside 
        -   header
        -   footer
        -   nav

### Headers and Footers 

Web authors have been labeling header and footer sections in their documents for years, so a dedicated header and footer elements have been created.

### Headers 

-   Used for introductory material that typically appears at the beginning of a web page or at the top of a section or article.

        <body>
            <header>
                <img src="" alt="">
                <h1>
                    Nuts about Web Fonts
                </h1>
                <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/">Blog</a></li>
                        <li><a href="/">Shop</a></li>
                    </ul>
                </nav>
            </header>
            <!--page content-->
        </body>
<body>
    <header>
        <img src="" alt="">
        <h1>
            Nuts about Web Fonts
        </h1>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/">Blog</a></li>
                <li><a href="/">Shop</a></li>
            </ul>
        </nav>
    </header>
    <!--page content-->
</body>

-   When used in an individual article, the __header__ might include:
    1.  article title
    2.  author
    3.  publication date

            <article>
                <header>
                    <h1>
                        More about WOFF
                    </h1>
                    <p>
                        by Jennifer Robbins, <time datetime="2017-11-11">November 11, 2017</time>
                    </p>
                </header>
                <!-- article content here -->
            </article>
<article>
    <header>
        <h1>
            More about WOFF
        </h1>
        <p>
            by Jennifer Robbins, <time datetime="2017-11-11">November 11, 2017</time>
        </p>
    </header>
    <!-- article content here -->
</article>

### Footers 

-   Used to indicate the type of information that typically comes at the end of a page or an article, such as:
    -   the author
    -   copyright
    -   information 
    -   related documents
    -   navigation

-   The footer element may apply to the entire document or it could be associated with a particular section or article.

-   If the footer is contained directly within the body element, either before or after all the other body content, then it applies to the entire page or application.

-   If it is contained in a sectioning element (section, article, nav, or aside), it is parsed as the footer for just that section.

-   Not required to appear last in the document or sectioning element. It could also appear at or near the beginning if that makes sense.

        <article>
            <header>
                <h1>
                    More about WOFF
                </h1>
                <p>
                    by Jennifer Robbins, <time datetime="2025-9-6">September 6, 2025</time>
                </p>
            </header>
            <!-- article content here -->
            <footer>
                <p>
                    <small>
                        Copyright &copy;2025 Jennifer Robbins.
                    </small>
                </p>
                <nav>
                    <ul>
                        <li><a href="/">Previous</a></li>
                        <li><a href="/">Next</a></li>
                    </ul>
                </nav>
            </footer>
        </article>
<article>
    <header>
        <h1>
            More about WOFF
        </h1>
        <p>
            by Jennifer Robbins, <time datetime="2025-9-6">September 6, 2025</time>
        </p>
    </header>
    <!-- article content here -->
    <footer>
        <p>
            <small>
                Copyright &copy;2025 Jennifer Robbins.
            </small>
        </p>
        <nav>
            <ul>
                <li><a href="/">Previous</a></li>
                <li><a href="/">Next</a></li>
            </ul>
        </nav>
    </footer>
</article>

### Sections and Articles 

-   Long documents are easier to use when they are divided into smaller parts.

-   For example:

    -   Books are divided into chapters.

    -   Newspapers have sections:

        -   local news
        -   sports
        -   comics

-   To divide long web documents into sections use the section element.

-   Sections typically include a heading plus content that has meaningful  reason to be grouped together.

        <section>
            <h2>
                Typography Books
            </h2>
            <ul>
                <li>_</li>
            </ul>
        </section>

        <section>
            <h2>
                Online Tutorials
            </h2>
            <p>
                These are the best tutorials on the web.
            </p>
            <ul>
                <li>
                    _
                </li>
            </ul>
        </section>
<section>
    <h2>
        Typography Books
    </h2>
    <ul>
        <li>_</li>
    </ul>
</section>

<section>
    <h2>
        Online Tutorials
    </h2>
    <p>
        These are the best tutorials on the web.
    </p>
    <ul>
        <li>
            _
        </li>
    </ul>
</section>

-   It is useful for:
    -   magazine
    -   newspaper
    -   articles
    -   blog posts
    -   comments
    -   other items that could be extracted for external use

            <article>
                <h1>
                    Get to know Helvetica
                </h1>
                <section>
                    <h2>
                        History of Helvetica
                    </h2>
                    <p>
                        _
                    </p>
                </section>
                <section>
                    <h2>
                        Helvetica Today
                    </h2>
                    <p>
                        _
                    </p>
                </section>
            </article>

<article>
    <h1>
        Get to know Helvetica
    </h1>
    <section>
        <h2>
            History of Helvetica
        </h2>
        <p>
            _
        </p>
    </section>
    <section>
        <h2>
            Helvetica Today
        </h2>
        <p>
            _
        </p>
    </section>
</article>

-   A section in a web document might be composed of a number of articles:

        <section id="essays">

            <article>
                <h1>
                    A Fresh Look at Futura
                </h1>
                <p>
                    _
                </p>
            </article>

            <article>
                <h1>
                    Getting Personal with Humanist
                </h1>
                <p>
                    _
                </p>
            </article>

        </section>

<section id="essays">
    <article>
        <h1>
            A Fresh Look at Futura
        </h1>
        <p>
            _
        </p>
</article>

<article>
        <h1>
            Getting Personal with Humanist
        </h1>
        <p>
            _
        </p>
    </article>
</section>

-   The __section and article__ elements are easily confused, particularly because it is possible to nest one in the other and vice versa.

-   If the content is self-contained and could appear outside the current context, it is best marked up as an article.

### Aside (Sidebars)

-   Identifies content that is separate from, but tangentially related tom the surrounding content.

-   In print, its equivalent is a sidebar, but it couldn't be called 'sidebard' because putting something on the side is a presentational description, not semantic.

-   Aside can be used for pull quotes, background information, lists of links, callouts, or anything else that might be associated with (but not critical to) a document.

        <h1>
            Web Typography
        </h1>
        <p>
            Back in 1997, there were competing font formats and tools for making them...
        </p>
        <p>
            We now have a number of methods for using beautiful fonts on web pages...
        </p>
        <aside>
            <h2>
                Web Font Resources
            </h2>
            <ul>
                <li>
                    <a href="http://typekit.com/">
                        Typekit
                    </a>
                </li>
                <li>
                    <a href="http://fonts.google.com">
                        Google Fonts 
                    </a>
                </li>
            </ul>
        </aside>
    
<h1>
    Web Typography
</h1>
<p>
    Back in 1997, there were competing font formats and tools for making them...
</p>
<p>
    We now have a number of methods for using beautiful fonts on web pages...
</p>
<aside>
    <h2>
        Web Font Resources
    </h2>
    <ul>
        <li>
            <a href="http://typekit.com/">
                Typekit
            </a>
        </li>
        <li>
            <a href="http://fonts.google.com">
                Google Fonts 
            </a>
        </li>
    </ul>
</aside>

### Navigation 

-   The __nav__ element gives developers a semantic way to identify navigation for a site.

        <nav>
            <ul>
                <li><a href="/">Serif</a></li>
                <li><a href="/">Sans-serif</a></li>
                <li><a href="/">Script</a></li>
                <li><a href="/">Display</a></li>
                <li><a href="/">Dingbats</a></li>
            </ul>
        </nav>        

<nav>
    <ul>
        <li><a href="/">Serif</a></li>
        <li><a href="/">Sans-serif</a></li>
        <li><a href="/">Script</a></li>
        <li><a href="/">Display</a></li>
        <li><a href="/">Dingbats</a></li>
    </ul>
</nav>

-   Not all lists of links should be wrapped in __nav__ tags, but the specifications makes it clear that __nav__ should be used for links that provide primary navigation around a site.

### Addresses

-   Used to create an area for contact information for the author or maintainer of the document.

-   Generally placed at the end of the document or in a section or article within a document.

-   An address would be right at home in a footer element.

-   It is intended specifically for author contact information.

        <address>
            Contibuted by <a href="../authors/robbins/">Jennifer Robbins</a>,
            <a href="http://www.oreilly.com">O'Reilly Media</a>
        </address>

<address>
    Contibuted by <a href="../authors/robbins/">Jennifer Robbins</a>,
    <a href="http://www.oreilly.com">O'Reilly Media</a>
</address>

## THE INLINE ELEMENT ROUNDUP

Provide semantic meaning to phrases within the chunks by using what the HTML5 specification calls text-level semantic elements.

### Text-Level (inline) Elements

1.  Emphasized text

    -   use __em__ element to indicate which part of a sentence should be stressed or emphasized.

            <p>
                <em>Arlo</em>is very smart.
            </p>
            <p>
                Arlo is <em>very</em> smart.
            </p>
<p>
    <em>Arlo</em> is very smart.
</p>
<p>
    Arlo is <em>very</em> smart.
</p>

2.  Important text 

    -   use __strong__ element to indicate that a word or phrase is important, serious or urgent

            <p>
                When returning the car, <strong>drop the keys 
                inthe red box by the front desk.</strong>
            </p>
<p>
    When returning the car, <strong>drop the keys 
    inthe red box by the front desk.</strong>
</p>

3.  Elements originally named for their presentational properties

    -   __b element,__ keywords, product names, and other phrases that need to stand out from surrounding text without conveying added importance or emphasis.

            <p>
                The slabs at the ends of letter strokes are called <b>serifs</b>.
            </p>

    -   __i element,__ indicates text that is in a different voice or mood than the surrounding text, such as a phrase from another language, a technical term, or a thought.

            <p>
                Simply change the font and <i>Voila!</i>, a new personality!
            </p>

    -   __s element,__ indicates text is incorrect.

            <p>
                Scala Sans was designed by <s>Eric Gill</s> Martin Majoor.
            </p>

    -   __u element,__ used when the text has semantic significance, such as formal name

            <p>
                New York subway signage is set in <u>Helviteca</u>.
            </p>
    -   __small element,__ indicates an addendum or side note to the main text, such as the legal 'small print' at the bottom of a document.

            <p>
                <small>(This font is free for personal and commercial use.)</small>
            </p>

4.  Short quotations 

    -   __q element,__ adds a quotation mark to texts or phrases or whole sentences and mode.

            Matthew Carter says, <q>Our alphabet hasn't changed in eons.</q>

    -   According to HTML specifications, browsers should add quotation marks around q elements automatically, so you don't need to include them in the source document.

5.  Abbreviations and acronyms

    -   __abbr element,__ is used for abbreviations and acronyms

    -   Used for shortened versions of a word ending in a period.

    -   Example :

        Connecticut , Conn.

        United States of America , USA

    -   The title attribute provides the long version of the shortened term

            <abbr title="Points">pts.</abbr>
            <abbr title="American Type Founders">ATF</abbr> 

6.  Citations 

    -   Used to identify a reference to another document, such as a book, magazine, article title, and so on.

    -   Typically rendered in italic text by default.

            <p>
            Passages of this article were inspired by <cite> The Complete Manual of Typography</cite>
            by James Felici 
            </p>            

7.  Defining Terms
    
    -   __dfn element,__ point out the first and defining instance of a word in a document in some fashion.

            <p>
                <dfn>Script typefaces</dfn> are based on handwriting.
            </p>

8.  Program code elements 

    