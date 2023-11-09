#This program assign the area with appropriate Soil Conservation Structures
#To use create a folder "shp" in C: drive and paste the shapefiles with name input.shp and associate extension files.
# To know the content of file or format please refer code, as documentation is not prepared
import geopandas as gpd
import pandas as pd
import os

print("Place your shapefiles in a folder shp in C drive and name them input.shp...it will look like C:/shp/input.shp")
chk=input("press Y if you have done this, else press N:")
if(chk[0]!="y" and chk[0]!="Y"):
    quit()


#read the shapefile
vector = "C:\\shp\\input.shp"
gdf = gpd.read_file(vector)
            
# vector2 = "J:\\Project 8th sem\\Musakani MWS\\Musakani_MWS.shp"
# gdf02 = gpd.read_file(vector2)

#classify the table to create tables for each structure
gdf1 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Moderately steeply sloping (10-15 %)") | (gdf['New_Slope'] == "Steeply sloping (15-25 %)") ) & ((gdf['Soil_Depth'] == "Shallow (25-50 cm)")|(gdf['Soil_Depth'] == "Moderately deep (75-100 cm)")|(gdf['Soil_Depth'] == "Deep (100-150 cm)")) ] #staggerd trench >25
gdf2 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Moderately steeply sloping (10-15 %)") | (gdf['New_Slope'] == "Steeply sloping (15-25 %)") ) & ((gdf['Soil_Depth'] != "Shallow (25-50 cm)")&(gdf['Soil_Depth'] != "Moderately deep (75-100 cm)")&(gdf['Soil_Depth'] != "Deep (100-150 cm)")) ] #Trench cum bund <25
gdf3 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Very gently sloping (1-3%)") | (gdf['New_Slope'] == "Gently sloping (3-5%)") | (gdf['New_Slope'] == "Moderately sloping (5-10%)")) & ((gdf['Soil_Depth'] == "Shallow (25-50 cm)")|(gdf['Soil_Depth'] == "Moderately deep (75-100 cm)")|(gdf['Soil_Depth'] == "Deep (100-150 cm)")) ] #stonebunding1 >25
gdf4 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Very gently sloping (1-3%)") | (gdf['New_Slope'] == "Gently sloping (3-5%)") | (gdf['New_Slope'] == "Moderately sloping (5-10%)")) & ((gdf['Soil_Depth'] != "Shallow (25-50 cm)")&(gdf['Soil_Depth'] != "Moderately deep (75-100 cm)")&(gdf['Soil_Depth'] != "Deep (100-150 cm)")) ] #stonebunding2 <25
gdf5 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Moderately steeply sloping (10-15 %)") | (gdf['New_Slope'] == "Steeply sloping (15-25 %)"))] #Terrace
gdf6 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Moderately sloping (5-10%)") )] #Gradedbund
gdf7 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Gently sloping (3-5%)") )] #Trench cum bund
gdf8 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Very gently sloping (1-3%)") )] #Field bunding
gdf9 = gdf[(gdf['New_Slope'] == "Strongly sloping (>25 %)")]    #plantation
gdf10= gdf[(gdf['LULC'] == "River")]
gdf11= gdf[(gdf['LULC'] == "Habitation")]
gdf12= gdf[(gdf['LULC'] == "Waterbody")]

chk2=input("Do you also want files for separate structures?")

directory = "Product"
parent_dir = "C:/shp/"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

# recreating the table
def add_code(df,code,s):
    rows = len(df)
    id=[]
    nm=[]
    for i in range(rows):
        id.append(code)
        nm.append(s)
    df['StructureId'] = id
    df['StructureName'] = nm
    if(chk[0]=='y' or chk[0]=='Y'):
        df.to_file(f"C:\\shp\\Product\\{s}.shp")
    return df
    


gdf1 = add_code(gdf1,1,"staggerd Trench")
gdf2 = add_code(gdf2,2,"Trench cum bund - NA")
gdf3 = add_code(gdf3,3,"stonebunding1 ")
gdf4 = add_code(gdf4,4,"stonebunding2 ")
gdf5 = add_code(gdf5,5,"Terrace ")
gdf6 = add_code(gdf6,6,"Graded bund ")
gdf7 = add_code(gdf7,7,"Trench cum bund - A")
gdf8 = add_code(gdf8,8,"Field bunding")
gdf9 = add_code(gdf9,9,"plantation")
gdf10 = add_code(gdf10,10,"River")
gdf11 = add_code(gdf11,11,"Habitation")
gdf12 = add_code(gdf12,12,"Waterbody")
gdff = pd.concat([gdf1,gdf2,gdf3,gdf4,gdf5,gdf6,gdf7,gdf8,gdf9,gdf10,gdf11,gdf12])
gdff.to_file("C:\\shp\\Product.shp.zip")

print("Process Completed !!!")
print("Your files has been saved into C:/shp folder")






