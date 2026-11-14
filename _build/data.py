TAG = "theelevatedcartweb-20"
STORE = "https://www.amazon.com/shop/thecareermo0c?tag=theelevatedcartweb-20"
ROOMS_STORE = "https://www.amazon.com/shop/thecareermo0c/curation/4c97f32f-8562-4177-b4cb-db1adc5a1992?tag=theelevatedcartweb-20"
CDN = "https://m.media-amazon.com/images/S/shoppable-media-external-prod-iad-us-east-1/"
PHOTO = "https://www.amazon.com/shop/thecareermo0c/photo/amzn1.shoppablemedia.v1."

# short product names keyed by ASIN
P = {
 "B0GTMQQFYZ":"Oversized modular cloud sectional, beige","B0C4C3VPPL":"Loloi Darby hand-knotted rug, sand","B0H9XJPPK9":"Round light oak coffee table","B0G8H85L4T":"Stone-look table lamps, set of 2","B07GSBW1RK":"Kate and Laurel gold frame set of 3","B0DBM3BJL6":"Half-round rattan pendant",
 "B0897VQ1LD":"Safavieh Kazumi rattan accent chair","B07MGKF9WB":"Chinoiserie ceramic urn","B0GS1CBJR1":"88\" slipcovered down-filled sofa","B07BF3F6B6":"Ginger jar table lamp","B09FFMWXKG":"Henn&Hart rectangular coffee table","B0D9T475X9":"Blue floral pillow cover",
 "B08Z8HVLFL":"Safavieh Metro wool rug, beige","B0H5CKFVYT":"89\" farmhouse fabric sofa","B0B9S3LNCQ":"Boucle swivel barrel chair","B0F6YD9Y22":"Round nesting coffee tables, set of 2","B07TR3N7ZW":"Gold arc floor lamp","B0DK525FFP":"Black boho lumbar pillow covers",
 "B0CW8YJXG2":"Expandable round dining table","B0F8Z7R7JT":"Upholstered dining chairs, set of 2","B0BVXHZBXD":"Hand-knotted area rug","B0DCB8L72X":"Woven rattan placemats, set of 12","B0BSF54KPS":"Fringe cloth napkins, set of 12","B07BF1TF54":"Classic ceramic urn lamp",
 "B0FCS74KXG":"Cloud modular sectional, 100.5\"","B0FHHB3ZNN":"Barrel swivel accent chair","B0DNCQQ4J8":"Rattan and mango wood coffee table","B0FMF1XJ5G":"Window pane wall mirror","B0FVSD1WCV":"7 ft faux olive tree","B0DN4THDYH":"Rattan pendant light",
 "B0FL1NRT5W":"86\" narrow farmhouse dining table","B0CW4CYY2C":"Loloi Magnolia Home Gigi rug","B0GZ4HRGNZ":"Retro modern dining chairs, set of 2","B0BFVHZRSF":"6-light brass chandelier","B0GB8FFQJY":"Linen check table runner","B0GJJJC3BP":"Clear glass hurricane holder",
 "B0GMVJ32ZJ":"Solid wood platform bed","B0B84LHZ99":"Angelica collection rug 6x9","B0CLYVJTDL":"Nourison sand ceramic table lamp","B0BS75H57L":"Montauk 2-drawer nightstand","B01L8BZIMO":"French flax linen duvet cover","B09SHDKVMF":"Framed canvas landscape art",
 "B0GCMCB67M":"86\" narrow dining table","B095Z3LWCB":"Reclaimed solid wood dining table","B0D7ZWDTJG":"Gold wagon wheel chandelier","B0GWCZ13FT":"Large black ceramic vase","B0GGB6FWR2":"Glass dome hurricanes, set of 2",
 "B0FXGQVXGV":"Large framed vintage wall art","B0G255NLXB":"Chunky chenille knit throw","B0G1Y736R6":"Solid wood queen platform bed","B0F1M3HK7H":"Modern farmhouse nightstand","B0B9HH5TCG":"Simplihome Amherst bedside table",
 "B0FSKL5257":"Oak and rattan sideboard","B0D1LP2K5Z":"Cascais 72\" dining table","B0G6Z4KK8H":"Clear glass globe pendant","B0H39M1Y7L":"Faux fall branches, set of 6","B0DM9NFVRK":"Tall white ceramic vase","B0CSSVRCWK":"Hand-forged decorative accent",
 "B0CLSY54SD":"12-light black wagon wheel chandelier","B0D2Y8HJMR":"Simplihome Connaught sideboard","B0F13RH2CM":"White ceramic farmhouse lamp","B08BJD4Y9P":"Reclaimed pine 94\" dining table",
 "B0FYV1Q29S":"Gold bamboo framed wall art","B0FQJN4YMR":"Textured gold framed art","B0H242BWFB":"Fall pillow covers, set of 2","B0H6Q8DBSP":"Brass arc reading lamp","B0GWJ5RPG9":"Vintage gold framed tree art",
 "B0GBVC9WWB":"Modular sectional loveseat","B0B74T71ND":"Jute and cotton hand-woven rug","B07G1B6WT9":"72\" shaker bookcase, white","B0G64H6YT1":"Faux hydrangea in vase","B0GGBR4TZG":"Battery wall sconces, set of 2",
 "B0GRGN77MV":"Large framed landscape canvas","B0D27JBMXJ":"Black decorative bowl","B0F8Q7SSYT":"Linen pillow covers, set of 2","B0GWR2NGV7":"Faux decorative books, set of 3",
 "B0DQ5SBW2Y":"Swivel barrel chair","B0F1FJSXHM":"Brushed nickel candle chandelier","B0H8N3G5LW":"Rattan wall sconce","B0GLZ4QM5Z":"Woven rattan urns, set of 2",
 "B0GYT15MS2":"Queen wood bed frame","B0FGPG2Q4H":"Farmhouse end table","B0DDQFXRKP":"24x24 gold picture frame","B0FG7P9J3F":"Ceramic vase with handles",
 "B0GWJHM54G":"Faux olive branches, set of 6","B0FGMPKWSL":"Two's Company crane candle holder","B0FPF2FQV4":"Large brushed gold round mirror","B0F33N3J9W":"Safavieh Hazel rug","B0GVS552M5":"Mid-century wood dining chairs, set of 4",
 "B0GRTZS1B9":"113\" modular sectional","B0F26CVFBR":"Waterproof pillow covers","B0G4GQ3BGM":"Vintage floral pillow covers","B0FDKRPYQ6":"Coastal scalloped pillow cover",
 "B0FX9ZWF9V":"Large farmhouse dining table","B0G1H15JY6":"Modern buffet cabinet","B0D2116SPT":"Upholstered curved dining chair","B0B6YNG56P":"Metal picture frame","B0GTVDBNLH":"Tall white ceramic vase",
 "B0CFYFCZ76":"Bedsure quilted bedspread","B0DKSZYQ5F":"Cotton waffle duvet cover set","B0GQR4HYHR":"White pinch-pleat linen curtains","B0GGR888HN":"Ceramic jar lamps, set of 2","B0GR4PYCW7":"Boho nightstands, set of 2",
 "B08BZBHLBR":"Bedsure textured cream throw","B0DJDMDWCR":"Loloi x CLJ Morris pillow cover","B0CSPVLDKB":"Loloi x CLJ Dinah pillow cover","B0DMXXTWLS":"Loloi ivory and beige pillow cover","B0DT6V6F33":"Cream boucle lumbar cover","B0GDF6Y7QZ":"Cream faux fur pillow cover",
 "B003X5IC6S":"Nourison natural beige rug 6x9","B0CJG2XLTS":"Classic berber rug 5x8","B0FCFQHDD8":"Beige ceramic vase with handles","B0G5842TW7":"Decorative books, set of 3","B0H2TYNT31":"Merax 42\" console with drawers","B0D78P6XCG":"Rattan serving tray",
 "B09B73DL7Q":"Gold bamboo napkin rings, set of 12","B0D14S1RNR":"Linen fringe Christmas pillow covers","B07V2BR4BZ":"Safavieh knit pillow, natural","B0D3HF6GBJ":"Large stone-look decorative bowl","B0DPCGS6FB":"French floral pillow covers",
}

# (slug, title, category, blurb, cdn image path, photo id, key ASINs)
ROOMS = [
 ("warm-neutral-living-room","The Warm Neutral Living Room","Living Room","A deep cloud sectional, a round oak coffee table and a rattan pendant. Layered, soft and made for real life.","ef58c06e-5b56-4d1c-bc63-8c7667ffcf1a/16fa0-ea7b-41aa-a1d7-5569f0bac._AC_._SX1200_SCLZZZZZZZ_.png","bd0139e6-a381-44dc-ad2b-e7545a021d8b",["B0GTMQQFYZ","B0C4C3VPPL","B0H9XJPPK9","B0G8H85L4T","B07GSBW1RK","B0DBM3BJL6"]),
 ("blue-and-white-living-room","The Blue and White Living Room","Living Room","Classic blue and white with chinoiserie, a slipcovered sofa and a rattan chair. Timeless and a little coastal.","9c34dfb6-5465-4648-bbef-29b25265eded/6e73c-482c-408f-888f-8d59c9fa9._AC_._SX1200_SCLZZZZZZZ_.png","fbc06ba7-2c8c-4424-9935-0cf1d94a54ac",["B0GS1CBJR1","B0897VQ1LD","B07MGKF9WB","B07BF3F6B6","B09FFMWXKG","B0D9T475X9"]),
 ("modern-organic-living-room","The Modern Organic Living Room","Living Room","Creamy upholstery, woven nesting tables and crisp black accents for contrast.","d94344b9-9d80-4248-b81d-c476245e9ab7/b9dd0-c40a-45c0-99f9-fa003b9aa._AC_._SX1200_SCLZZZZZZZ_.png","79c9ddd3-4578-4e74-a0d0-d28192e1486f",["B0H5CKFVYT","B0B9S3LNCQ","B0F6YD9Y22","B08Z8HVLFL","B07TR3N7ZW","B0DK525FFP"]),
 ("blue-rattan-dining-nook","The Blue and Rattan Dining Nook","Dining","A round table set with woven placemats, fringe napkins and fresh hydrangeas.","233ed8c0-f152-4d46-95e6-d08e96dafaa1/931fc-d0b5-44d4-b5df-c04c1680c._AC_._SX1200_SCLZZZZZZZ_.png","b4105a5a-00a8-4b55-8a2c-65cb7f87c14d",["B0CW8YJXG2","B0F8Z7R7JT","B0BVXHZBXD","B0DCB8L72X","B0BSF54KPS","B07BF1TF54"]),
 ("light-and-airy-living-room","The Light and Airy Living Room","Living Room","A cloud sectional, barrel chairs and a big olive tree in a room full of light.","5af9e876-9cb6-423c-839d-30486cfde9b0/90d51-06ef-4e3f-b266-8e509d20f._AC_._SX1200_SCLZZZZZZZ_.jpeg","a18a397d-c336-4bc1-93a9-a92d6034e01a",["B0FCS74KXG","B0FHHB3ZNN","B0DNCQQ4J8","B0FMF1XJ5G","B0FVSD1WCV","B0DN4THDYH"]),
 ("classic-farmhouse-dining-room","The Classic Farmhouse Dining Room","Dining","A long narrow table, a soft vintage-look rug and a brass chandelier overhead.","1e6df03b-9bbb-4be6-a609-0aeb142b4087/43295-d846-490f-a21f-feae2317a._AC_._SX1200_SCLZZZZZZZ_.png","f3cdb815-2ee0-45b8-b2d1-52ea44d41ef6",["B0FL1NRT5W","B0CW4CYY2C","B0GZ4HRGNZ","B0BFVHZRSF","B0GB8FFQJY","B0GJJJC3BP"]),
 ("calm-neutral-bedroom","The Calm Neutral Bedroom","Bedroom","Warm wood, linen bedding and a soft landscape above the bed.","23ca78e5-0b0e-4892-927f-0f71653736dd/60be3-e2d2-47f6-b6f6-e45738181._AC_._SX1200_SCLZZZZZZZ_.png","a10481f7-ead0-4d39-a7ca-1b1fb8149db5",["B0GMVJ32ZJ","B01L8BZIMO","B0CLYVJTDL","B0BS75H57L","B0B84LHZ99","B09SHDKVMF"]),
 ("moody-dining-room","The Moody Dining Room","Dining","Deep walls, a reclaimed wood table and a gold wagon wheel chandelier.","41e653f4-4067-4ad0-a3bb-4e435b80138d/78a10-0228-4a77-9c37-a2d52bf9a._AC_._SX1200_SCLZZZZZZZ_.png","4d12d81f-45ce-4c68-a797-5b1198d7257e",["B095Z3LWCB","B0D7ZWDTJG","B0GCMCB67M","B0GWCZ13FT","B0GGB6FWR2"]),
 ("cozy-woven-bedroom","The Cozy Woven Bedroom","Bedroom","A woven pendant, a chunky knit throw and vintage art for a bedroom that feels collected.","085f1ca7-56da-4b6f-be78-03b6fce2e517/ea952-d5be-45a1-a560-5f15ab0bc._AC_._SX1200_SCLZZZZZZZ_.png","d62e2ec3-b572-43f3-808e-70860297445b",["B0G1Y736R6","B0G255NLXB","B0CLYVJTDL","B0FXGQVXGV","B0F1M3HK7H","B0B9HH5TCG"]),
 ("harvest-farmhouse-table","The Harvest Farmhouse Table","Dining","An oak sideboard, glass globe pendants and fall branches. Ready for a crowd.","09d29be2-94e1-4401-a0ba-39c0ee5357c6/a76ea-4f56-4e24-9f63-9c7a0fbde._AC_._SX1200_SCLZZZZZZZ_.png","f8d1b03d-b678-403f-b920-eeecaf1475fb",["B0D1LP2K5Z","B0FSKL5257","B0G6Z4KK8H","B0H39M1Y7L","B0DM9NFVRK","B0CSSVRCWK"]),
 ("rustic-wagon-wheel-dining","The Rustic Wagon Wheel Dining Room","Dining","A long reclaimed pine table under a black wagon wheel chandelier.","c9bbf4de-2e8b-4e5b-a352-a103d460eb50/90adf-dc9d-41b9-84ee-1944de804._AC_._SX1200_SCLZZZZZZZ_.png","ea6446aa-8bef-4a4e-bc68-144e2d576531",["B08BJD4Y9P","B0CLSY54SD","B0D2Y8HJMR","B0F13RH2CM"]),
 ("gold-and-green-living-room","The Gold and Green Living Room","Living Room","Paneled walls, gold frames and warm fall pillows.","b53c2681-4e39-4638-8597-c1e97440c0bd/87472-90e5-418f-b2f4-4d7082814._AC_._SX1200_SCLZZZZZZZ_.png","8de013e2-479c-46c9-8dfa-f188206864f1",["B0FYV1Q29S","B0FQJN4YMR","B0GWJ5RPG9","B0H6Q8DBSP","B0H242BWFB"]),
 ("blue-gallery-wall-living-room","The Blue Gallery Wall Living Room","Living Room","A cozy loveseat, a shaker bookcase and a four-frame gallery wall.","19056895-3c8d-46a3-9e02-ebec9f96f20f/6dfd1-c4a1-4543-b960-9ea933e9d._AC_._SX1200_SCLZZZZZZZ_.jpeg","f761d7ab-db77-4978-9a6e-b1b7c328a67a",["B0GBVC9WWB","B0B74T71ND","B07G1B6WT9","B0GGBR4TZG","B0G64H6YT1"]),
 ("mountain-modern-living-room","The Mountain Modern Living Room","Living Room","Big windows, a chunky wood coffee table and warm, earthy layers.","67803e81-ee50-4b85-badf-cc7abd4fe23d/df5e8-8286-490f-8266-d22078c96._AC_._SX1200_SCLZZZZZZZ_.png","4c9b15c0-1603-408e-aaae-5da4869349d2",["B0F13RH2CM","B0GRGN77MV","B0D27JBMXJ","B0F8Q7SSYT","B0GWR2NGV7"]),
 ("coastal-sunroom","The Coastal Sunroom","Living Room","Swivel barrel chairs, rattan accents and a soft nickel chandelier.","0509c0c2-6955-4964-b8b2-8471178e3c67/8e1b3-2ece-4fc4-9ad8-e3b63f2c6._AC_._SX1200_SCLZZZZZZZ_.png","f97e50af-276e-4929-859c-61d95fd02a9a",["B0DQ5SBW2Y","B0F1FJSXHM","B0H8N3G5LW","B0GLZ4QM5Z"]),
 ("blue-and-white-bedroom","The Blue and White Bedroom","Bedroom","Navy and white bedding, a gold-framed print and a pair of oversized nightstands.","e8d4ac6d-d2c7-4d67-b51e-f02c101e11b8/8eb9e-9440-4dfb-9929-66aee3ac0._AC_._SX1200_SCLZZZZZZZ_.jpeg","d2ea57ea-5eae-4514-8af3-0a388d7aa977",["B0GYT15MS2","B0FGPG2Q4H","B0DDQFXRKP","B0FG7P9J3F"]),
 ("sunlit-oak-dining-room","The Sunlit Oak Dining Room","Dining","Light oak, a round gold mirror and olive branches on the sideboard.","0c96caff-d8c7-40cb-8f6b-e91508688461/05a80-8090-4923-ac35-c8dbc8cf1._AC_._SX1200_SCLZZZZZZZ_.jpeg","4c7f2edd-db33-4832-b720-b448f0cbb130",["B0FSKL5257","B0GVS552M5","B0FPF2FQV4","B0FGMPKWSL","B0GWJHM54G","B0F33N3J9W"]),
 ("coastal-cloud-couch","The Coastal Cloud Couch Living Room","Living Room","A sink-in sectional with blue and terracotta pillows by a wall of windows.","8be631bc-9739-4946-9b0f-61a9bf3d06bf/42efe-e530-4091-ba8e-d41f23616._AC_._SX1200_SCLZZZZZZZ_.jpeg","644a5455-4a8f-4b80-9c9d-01ac23bb61cf",["B0FCS74KXG","B0GRTZS1B9","B0G4GQ3BGM","B0FDKRPYQ6"]),
 ("bright-cream-dining-room","The Bright Cream Dining Room","Dining","Curved upholstered chairs, a warm rug and a glass pendant over a farmhouse table.","1eaaee20-4bc2-4327-ad3a-ac0c9e9eca81/f244a-8a47-4731-9ec7-bb7983f0c._AC_._SX1200_SCLZZZZZZZ_.jpeg","f4e1bd74-b4e4-496a-b730-7d1c5dd29943",["B0FX9ZWF9V","B0D2116SPT","B0G1H15JY6","B0GTVDBNLH","B0GGB6FWR2"]),
 ("crisp-white-bedroom","The Crisp White Bedroom","Bedroom","A quilted bedspread, waffle duvet and long linen drapes. Hotel calm at home.","e7197e63-fc87-4a16-88e9-037cc4cdaa52/d7755-dacf-4f56-b109-93a654e4a._AC_._SX1200_SCLZZZZZZZ_.jpeg","e92b122d-8eaf-4867-9318-de78edbcc8e4",["B0CFYFCZ76","B0DKSZYQ5F","B0GQR4HYHR","B0GGR888HN","B0GR4PYCW7"]),
 ("farmhouse-striped-chair-living-room","The Farmhouse Living Room","Living Room","A slipcovered sofa, a striped accent chair, blue Loloi pillows and a brushed brass chandelier over a warm red rug.","e15d1fd5-e73d-431d-aa96-6074ea036070/15d35-cfbd-4b77-bc85-e698aa559._AC_._SX1200_SCLZZZZZZZ_.png","5f1984ee-ebb8-447d-9b73-7d7cc95a7b0f",["B0H8XV2KJH","B0C6LHK6LG","B0HDRPY4N4","B0H1L29HKW","B0H5HX75HQ","B06XVSZVN1","B0DJDN6BLC","B0FPH8TZZT","B0FR73QXPY"]),
]

P.update({
 "B0H8XV2KJH":"89\" slipcovered farmhouse sofa","B0C6LHK6LG":"Striped farmhouse accent chair","B0HDRPY4N4":"47\" farmhouse coffee table","B0H1L29HKW":"Red oriental washable rug, 6x9","B0H5HX75HQ":"Brushed brass chandelier","B06XVSZVN1":"Brass adjustable floor lamp","B0DJDN6BLC":"Loloi x CLJ Auggie blue pillow","B0FPH8TZZT":"Loloi x CLJ Marigold blue pillow","B0FR73QXPY":"Loloi x Amber Lewis Blair pillow",
})

P.update({
 "B0H73QQ1ZW":"Burgundy velvet stockings, set of 2","B0H1H2FC81":"Emerald velvet stockings, set of 2","B0H5WF2C2V":"Velvet ornament set, 51 pieces","B0FP16QMYR":"Burgundy velvet ribbon bows, set of 12","B0H944MSM5":"Dark green velvet bows, set of 24","B0H8DDHBQG":"Burgundy bow garland, 6.6 ft","B0H1H5XMCM":"Dark green plaid pillow covers, set of 2","B0CF8M84YY":"Red and green plaid table runner","B0F9XDDL8Z":"Green tartan cloth napkins, set of 4","B01HV82VGO":"Spode Christmas Tree dinner plates, set of 4","B0H39BFCKF":"Plaid ruffled tree skirt","B0FHD8JSWQ":"Gold vintage-style Christmas decor","B08FY34VR2":"Vintage ceramic tree night light","B0H9WRK78C":"Vintage velvet Christmas tree decor",
 "B0FB3F3TLM":"Fall eucalyptus wreath, 26\"","B0HK7DWHK5":"Green plaid Thanksgiving napkins","B0HK76T5C9":"Green plaid Thanksgiving table linen","B0DGD15VMG":"Woven round placemats, set of 6","B09NSNMRST":"Rustic farmhouse napkin rings, set of 6","B0DSGGBP1K":"Fall Countryside tablecloth","B0DSGGFF83":"Fall Countryside napkins, set of 4","B0DZ2N1MHZ":"Faux floral table centerpiece","B0B7DKVC9Z":"Velvet pumpkin pillows","B0D9L1HRY8":"Spode Woodland nesting trays","B0FC2CC8HM":"Pumpkin crystal salt and pepper","B0DH5Y5SVJ":"White turkey decorative accent","B0DRDNV7HX":"Vintage amber tumblers",
})
XMAS_LIST="https://www.amazon.com/shop/thecareermo0c/list/C1TJ6GQOJRLL?tag="+TAG
TG_LIST="https://www.amazon.com/shop/thecareermo0c/list/1V3PYPXNW7SDO?tag="+TAG
P.update({
 "B0HGF94N1P":"Cedar garland, 9 ft","B0GRNM5P7K":"Pure linen table runner, 18 x 90","B0CH9Z8DXC":"Ceramic Christmas tree dinner plates","B0H8DMZC1D":"Christmas tree dinnerware set","B0HGR6ZR73":"Nutcracker soldier salt and pepper","B0H97XDCTN":"Cotton cloth napkins, set of 4","B081CS1RGG":"Christmas paper napkins","B0CH6LK53Y":"Cordless table lamps","B0H5QX71X8":"Vintage beaded charger plates","B0GZ5LFN4M":"Crystal goblets, set of 2","B08LR4GFMX":"Ruby red cut wine glasses",
 "B0HK7DWHK5":"Green plaid tablecloth, 60 x 84","B0HK76T5C9":"Green plaid napkins, set of 4","B0H1PTKC7M":"Vintage turkey plates, 32 pieces","B0H83SRTSL":"Glass pumpkin dome cake stands, set of 2","B007A2ZBZU":"Gold cutlery set","B0DVGT378N":"Gold hand-forged taper holder","B0D47Q2ZWW":"Fluted LED taper candles","B0DH5Y5SVJ":"White stoneware turkey jar",
 "B0H836ZTQN":"Haunted house table runner, 13 x 72",
 "B0725FZMLQ":"Holly wreath Christmas pillow","B07M9ZL1WF":"Safavieh Gwendolen poinsettia pillow","B0F2JNT1BV":"Loloi x Jeremiah Brent Leroy brown pillow","B0DDVH9TDC":"Loloi dark olive pillow","B0HBC6NN18":"White Stewart plaid faux fur pillow cover","B0HBC2BM37":"Red Stewart plaid faux fur pillow cover",
})
XMAS_LIST="https://www.amazon.com/shop/thecareermo0c/list/C1TJ6GQOJRLL?tag="+TAG
TG_LIST="https://www.amazon.com/shop/thecareermo0c/list/1V3PYPXNW7SDO?tag="+TAG
HAL_LIST="https://www.amazon.com/shop/thecareermo0c/list/3FMC6YQXBG4FY?tag="+TAG
# (slug,title,hol,blurb,image ref,ASINs or None,room index or None, shop override url or None)
HROOMS=[
 ("christmas-tablescape","The Classic Christmas Tablescape","christmas","Cedar garland down a linen runner, Christmas tree plates, beaded chargers and ruby glassware.","cdn:a460a3e3-1e90-4df1-933e-c47d95b5862c/47d09-7de8-419d-8867-305059399._AC_._SX1200_SCLZZZZZZZ_.png",["B0HGF94N1P","B0GRNM5P7K","B0CH9Z8DXC","B0H5QX71X8","B0GZ5LFN4M","B08LR4GFMX","B0HGR6ZR73","B0H97XDCTN","B0CH6LK53Y"],None,PHOTO+"b2f2eae7-de3a-4576-bd71-03ac34d41b8f?tag="+TAG),
 ("christmas-pillows","The Pottery Barn Inspired Holiday Pillow Stack","christmas","A holly wreath, a red poinsettia and classic tartan plaid. Timeless holiday pillows for less.","img:christmas-pillows",["B0725FZMLQ","B0F2JNT1BV","B07M9ZL1WF","B0HBC6NN18","B0HBC2BM37","B0DDVH9TDC"],None,XMAS_LIST),
 ("thanksgiving-turkey-table","The Vintage Turkey Thanksgiving Table","thanksgiving","Green plaid linens, vintage turkey plates, a glass pumpkin dome and amber glasses.","img:thanksgiving-turkey-table",["B0HK7DWHK5","B0HK76T5C9","B0H1PTKC7M","B0DGD15VMG","B0H83SRTSL","B0FC2CC8HM","B0DH5Y5SVJ","B0DRDNV7HX","B0DZ2N1MHZ","B0DVGT378N","B007A2ZBZU"],None,TG_LIST),
 ("harvest-farmhouse-table","The Harvest Farmhouse Table","thanksgiving","An oak sideboard, glass globe pendants and fall branches. Ready for a crowd.","room:9",None,9,None),
 ("fall-living-room","The Fall Living Room","thanksgiving","Paneled walls, gold frames and warm fall pillows. Cozy from October through Thanksgiving.","room:11",None,11,None),
 ("haunted-manor-table","The Haunted Manor Halloween Table","halloween","A haunted house runner, black taper candles and moody dinnerware for a chic Halloween table.","img:halloween-haunted-manor",["B0H836ZTQN"],None,HAL_LIST),
]

P.update({"B0DJVV3GMP":"Easly 77\" x 38\" arched floor mirror, gold","B0CT9WGRDY":"Nathan James Beacon woven counter stools, set of 2","B0GN9QJ47W":"Woven rope-back dining chairs, set of 2","B0HB497V91":"Nathan James Syd arched bookcase"})
# Prices checked 2026-11-13. BIG = $100+ pieces that get an "Add to cart" button (longer Amazon credit window).
BIG = set("""B01L8BZIMO B06XVSZVN1 B08BJD4Y9P B0897VQ1LD B07G1B6WT9 B08Z8HVLFL B09FFMWXKG B0B74T71ND B0B9HH5TCG B0BVXHZBXD B0BFVHZRSF B0BS75H57L B0C6LHK6LG B0C4C3VPPL B0CLSY54SD B0CW8YJXG2 B0CW4CYY2C B0D1LP2K5Z B0CT9WGRDY B0D2Y8HJMR B0DBM3BJL6 B0D7ZWDTJG B0DJVV3GMP B0DNCQQ4J8 B0DQ5SBW2Y B0DN4THDYH B0DM9NFVRK B0F13RH2CM B0F1FJSXHM B0F1M3HK7H B0F8Z7R7JT B0F6YD9Y22 B0FCS74KXG B0FGPG2Q4H B0FHHB3ZNN B0FL1NRT5W B0FPF2FQV4 B0FSKL5257 B0FVSD1WCV B0G1H15JY6 B0FX9ZWF9V B0G1Y736R6 B0GCMCB67M B0GBVC9WWB B0GN9QJ47W B0GLZ4QM5Z B0GR4PYCW7 B0GTMQQFYZ B0GS1CBJR1 B0GVS552M5 B0GYT15MS2 B0GZ4HRGNZ B0H1L29HKW B0H2TYNT31 B0H5CKFVYT B0H5HX75HQ B0H8N3G5LW B0HB497V91 B0HDRPY4N4""".split())
# Showing as unavailable on Amazon on 2026-11-13: hidden from shopping lists until back in stock or replaced.
UNAVAIL = set("""B095Z3LWCB B08BZBHLBR B0D2116SPT B0FGMPKWSL B0GMVJ32ZJ B0GRTZS1B9 B0H6Q8DBSP B0H8XV2KJH""".split())

P.update({"B0DZP1K85Z":"Red, white and blue dobby stripe runner","B0CTD5PMQX":"Woven rattan placemats, set of 4","B002S0RX1O":"Polish pottery blue stars dinner plate","B0GLPSYYGR":"Patriotic 10\" plates, set of 4","B0CX4XDV3Q":"4th of July pillow covers, set of 2","B0C7J1F1L2":"Weathered wood serving tray",
 "B06XTJ73XJ":"Classic USA stripe table runner","B07NR9SGR8":"Classic USA stripe napkins, set of 4","B0GXH212ZK":"Vintage Americana melamine salad bowl","B0GXGTW59Y":"Vintage Americana melamine tumblers","B07CYWKJRY":"Round woven placemats, set of 6","B0GVT6NNNY":"Patriotic chenille lumbar pillow covers, set of 2",
 "B0BRQM5BVT":"Red striped linen tablecloth, 60 x 90","B0CX1RM9KJ":"Red and blue stripe cloth napkins","B0D2G122BM":"Bonjour Fete cabana stripe dinner plates","B0767PG537":"Glass pitcher, 87 oz",
 "B0GXGVNP9S":"Americana tidbit plates","B0GXGRZT6C":"Americana accent plates","B0GXGS4JKQ":"Vintage Americana chip and dip set","B0GXGWNXBH":"Vintage Americana handled serving tray","B0GXH1LB6G":"Vintage Americana pitcher","B0GW1KTZ4Y":"Striped melamine dinnerware set for 4",
 "B0D1GBYSKB":"American flag string lights","B088FLY7S8":"Small American flags, 12 pack","B0GSHPSNK1":"Patriotic wreath sash, set of 2","B0BW229LQ6":"Tossed stars patriotic tablecloth"})
JULY4_LIST="https://www.amazon.com/shop/thecareermo0c/list/3TB9V3TFIEVT?tag="+TAG
HROOMS += [
 ("july4-poolside-patio","The Poolside Americana Patio","fourth","Rattan chairs, navy star pillows, a striped runner and blue hydrangeas for a relaxed Fourth by the pool.","img:july4-poolside-patio",["B0DZP1K85Z","B0CTD5PMQX","B002S0RX1O","B0GLPSYYGR","B0CX4XDV3Q","B0C7J1F1L2"],None,JULY4_LIST),
 ("july4-americana-patio-table","The Americana Patio Dinner Table","fourth","A classic USA stripe runner, woven placemats and vintage Americana serveware for summer dinner parties.","img:july4-americana-patio-table",["B06XTJ73XJ","B07NR9SGR8","B07CYWKJRY","B0GXH212ZK","B0GXGTW59Y","B0GVT6NNNY"],None,JULY4_LIST),
 ("july4-red-white-blue-tablescape","The Red, White and Blue Outdoor Tablescape","fourth","A red striped linen tablecloth, cabana stripe plates and woven placemats under string lights.","img:july4-red-white-blue-tablescape",["B0BRQM5BVT","B0D2G122BM","B07CYWKJRY","B0CX1RM9KJ","B0767PG537"],None,JULY4_LIST),
 ("july4-americana-dinnerware","Vintage Americana Dinnerware","fourth","Mix-and-match stars and stripes plates, pitchers and serveware that feel timeless from Memorial Day through Labor Day.","img:july4-americana-dinnerware",["B0GXGVNP9S","B0GXGRZT6C","B0GXGS4JKQ","B0GXGWNXBH","B0GXH1LB6G","B002S0RX1O","B0GW1KTZ4Y"],None,JULY4_LIST),
 ("july4-americana-porch","The Classic Americana Porch","fourth","A flag on the porch, patriotic pillows, flag string lights and a stars tablecloth for Fourth of July hosting.","img:july4-americana-porch",["B0GVT6NNNY","B0D1GBYSKB","B088FLY7S8","B0GSHPSNK1","B0BW229LQ6","B0DZP1K85Z"],None,JULY4_LIST),
]
P.update({"B0GY78DPJR": "47 inch round reclaimed pine pedestal dining table", "B0DMT47JKY": "Rattan door entry cabinet, light oak",
          "B0GLGM4DLX": "42 inch water hyacinth storage trunk", "B0F1ZDBLKM": "Square glass top coffee table with rattan shelf",
          "B0FBPYM3XD": "22 inch rattan 3 tier nightstand"})
BIG |= {"B0GY78DPJR", "B0DMT47JKY", "B0GLGM4DLX", "B0F1ZDBLKM", "B0FBPYM3XD"}
P.update({"B0C1L968KY": "Woven back counter stool", "B0DWJMTD62": "Beige barrel dining chairs on casters, set of 2"})
BIG |= {"B0DWJMTD62"}
P.update({"B0GGQX2LQS": "Rattan headboard queen bed frame", "B0FNCSSGRZ": "Oversized swivel barrel chair, beige chenille"})
BIG |= {"B0GGQX2LQS", "B0FNCSSGRZ"}

P.update({"B0CWH5GL6L":"Round fluted drum coffee table, oak","B0HFS1RWTZ":"Cane back dining chairs, set of 2"})
BIG |= {"B0CWH5GL6L", "B0HFS1RWTZ"}
P.update({"B0DNT1GDW7":"White cotton quilt set, king"})
BIG |= {"B0DNT1GDW7"}
P.update({"B09LDG97WH":"Meridian Oakhill solid mango fluted coffee table, 36\""})
BIG |= {"B09LDG97WH"}
