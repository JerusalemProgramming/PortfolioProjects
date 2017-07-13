MongoDBCollectionDocument_1B = { ## PYTHON DICTIONARY OBJECT // MONGO DB DOCUMENT OBJECT // JSON OBJECT

	'Item_ID_NameOfDealer' : 'A_1234567',  ## Internal Item ID Number used by Dealer
	'Item_Path2Picture' : '/images/img1.jpg', ## Computer file path to image/picture file of the Item
	'Item_ID_IAA' : 'NA', ## ID Number used by the Israel Antiquities Authority (IAA) to catalog and track Items from many separate Dealers
	'Item_IsImport' : 'NA', ## Is the Item an import thus requiring Import Approval (IA) ID number (below)
	'Item_ID_IA' : 'NA', ## If the Item is an import, then this is the Import Approval (IA) ID number.
	'Item_IsExport' : 'NA', ## Is the Item an export thus requiring Export Approval (EA) ID number (below)
	'Item_ID_EA' : 'NA', ## If the Item is an export, then this is the Export Approval (EA) ID number
	'Item_Civilization' : 'NA', ## Ancient civilization info of the Item
	'Item_Title' : 'NA', ## Title info of the Item
	'Item_Description' : 'NA', ## Description info of the Item
	'Item_DateAncient' : 'NA', ## Ancient date info of the Item
	'Item_Type' : 'NA', ## Type / category info of the Item within Dealer's classification of types/categories
	'Item_SizeHxW' : 'NA',	## Size HxW info of the Item
	'Item_Condition' : 'NA', ## Condition info of the Item
	'Item_Reference' : 'NA', ## Academic book-references-&-citations info relevant to the Item - if any
	'Item_Provenance' : 'NA', ## Provenance info of the Item
	'Item_MannerOfAcquisition' : 'NA', ## Manner of Acquisition info of the Item, i.e. from where was Item purchased?	
	'Item_DateOfAcquisition' : 'NA', ## Date of Acquisition info of the Item
	
	'Item_IsSold' : 'NA', ## Is the Item sold?  ## SOLD // NOT SOLD
	'Item_SalesInvoiceNumber' : 'NA', ## If sold, then Sales Invoice Number of Item
	'Item_Profit' : 'NA', ## If sold, then Profit of Item to be calculated with Item_CostPrice and Item_SalePrices fields (below)
	
	'Item_DateSold2Client' : 'NA',	## If sold, then Date sold to Client
  	'Item_Sold2WhichClient' : {  ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
		'Client_ContactDetails': {  ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
			'Client_NameLast' : 'NA', ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
			'Client_NameFirst' : 'NA', ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
			'Client_Address' : 'NA', ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
			'Client_Telephone' : 'NA', ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
			'Client_Email' : 'NA' ## If sold, then Sold to which Client?  i.e. details of Client who purchased the Item
		}
	 }
    	
	'Item_CostPrice' : 'NA', ## Cost Price of the Item
	'Item_SalePrice' : 'NA', ## If sold, then Sale Price of the Item
	'Item_ShippingCosts' : 'NA', ## If sold, then Shipping Costs of sending the Item to Client - if any
	'Item_DidPurchaseIncludeVAT' : 'NA', ## Did Purchase of Item include VAT (e.g. either within Israel or VAT in purchase overseas)?
	'Item_VATPURCHASE_HowMuch' : 'NA', ## If Purchase of Item includes VAT, then How Much VAT was paid (% PERCENTAGE)?
	'Item_DidSaleIncludeVAT' : 'NA', ## Did Sale of Item include VAT (e.g. either within Israel or VAT in sale overseas)?
	'Item_VATSALE_HowMuch' : 'NA',	## If Sale of Item included VAT, then How Much VAT was paid (% PERCENTAGE)?
		
	'Item_ID_2ndShop' : 'NA', ## Internal Item ID Number used by Dealer - These last 5 Database Key:Value pairs were necessary for prior steps of extracting & merging inventory database info from Dealer's two (2) web sites & internal inventory Excel file (with multiple sheets):  1.) Data was exported to CSV files, 2.) Custom Python programming to Extract, Transform, Load (ETL) = Input Data, Process Data, Output Data
	'Item_IsImport_2ndShop' : 'NA',	## Is the Item an import thus requiring Import Approval (IA) ID number (above); These last 5 Database Key:Value pairs served as good test controls to confirm integrity of info after extracting & merging inventory database info from Dealer's two (2) web sites & internal inventory Excel file (with multiple sheets)
	'Item_Title_2ndShop' : 'NA', ## Title of the Item on the Dealer's 2nd web site
	'Item_SalePrice_2ndShop' : 'NA', ## If sold, then Sale Price of the Item on the Dealer's 2nd web site.  This Key:Value pair serves as good test control to test with Item_SalePrice field (above) to confirm integrity of info after extracting & merging database info from Dealer's two (2) web sites & internal inventory Excel file (with multiple sheets)
	'Item_IsInStock_2ndShop' : 'NA' ## Is the Item In Stock on the Dealer's 2nd web site?  This Key:Value pair serves as good test control to test with Item_IsSold field (above) to confirm integrity of info after extracting & merging inventory database info from Dealer's two (2) web sites & internal inventory Excel File (with multiple sheets)

}
