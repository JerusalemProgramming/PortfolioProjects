# PortfolioProjects
PortfolioProjects, Examples of Coding Work

I was tasked to create a custom Inventory-Client Database program (in Python with Mongo DB via PyMongo) that needed to manage inventory of local antiquities dealer here in Jerusalem, as well as to track sales of each item to specific client if/when an item was sold.  Dealer wanted the inventory database to calculate total cost and profit of the entire inventory which meant that each item's cost and profit had to be calculated first individually.  Additionally the dealer wanted this custom Inventory-Client Database to automatically generate invoices for each sale of item(s) to each client so that these automatically-generated invoice files could be delivered to Accountant-Tax-Attorney as either BULK PDF/DOC FILES and/or BULK PRINTED INVOICES for tax returns at the end of each fiscal business year's cost/profit calculations.

Because "Content is King" for Big Data Science Programming, the most critical and basic first step was to design & architect the database around logical organization of the data.  We needed to track Items of antiquities, and each Item could be sold to only one Client.

As we were developing a custom database that tracked Dealer's inventory of Items, it was only logical to use "Item_" as the prefix for the variable names that we would be creating for the Python Dictionary Object // Mongo DB Document Object // JSON Object Key:Value item pairs.

Naturally each "Item_" could possibly be sold to only one (1) "Client_" if/when that Item in inventory becomes sold.  If sold, then it would be necessary to update "Item_Sold2WhichClient" field with "Client_" info who purchased the "Item_".  We would be updating "Item_Sold2WhichClient" field's value with "Client_ContactDetails" object that contains the following five (5) specific Key:Value details about each "Client_":  1.) "Client_NameLast", 2.) "Client_NameFirst", 3.) "Client_Address", 4.) "Client_Telephone", 5.) "Client_Email".

It would be possible to track if multiple Items were included in one (1) Sale to one (1) Client via the "Item_SalesInvoiceNumber" field:  i.e. if two (2) or more different Items in inventory have the same value for "Item_SalesInvoiceNumber", then these multiple Items are part of one (1) Sale to one (1) Client.

Being a self-taught programmer out of necessity to solve problems, I taught myself to program in Python by separating code into functions, and then separating functions into Python modules that could then be accessed with OBJECT.METHOD DOT.NOTATION.  I thus have come to program in a certain Pythonic Procedural Programming style of importing modules with functions defined within those modules, and then calling functions that are specific to each module as necessary.  I prefix all module names with "mod_" prefix, and I prefix all function names with "fn_" prefix, and I use the same descriptive name for both "mod_" and "fn_" names, thus allowing access via module-dot-function call via PYTHONIC MODULE.FUNCTION format (i.e. similar to CLASS OBJECTS, but without the need to bind data to those objects), i.e. Pythonic procedural functional programming that keeps data separate from functions as much as possible.

The main "root" and/or "__init__.py"-like and/or "flask_run.py"-like initial file for this program has been prefixed with variable prefix "program_", and it - in turn - imports and calls various modules with their "mod_" prefix, and functions within those modules via the "fn_" prefix with the OBJECT-ORIENTED MODULE.FUNCTION DOT.NOTATION.




