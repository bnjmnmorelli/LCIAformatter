import lciafmt
from lciafmt.util import store_method, save_json

method = lciafmt.Method.RECIPE_2016

#To obtain summary LCIA endpoint categories (damage assessment) set to True
apply_summary = False

def main():

    data = lciafmt.get_method(method, endpoint = False, 
                              summary = False)
    data_endpoint = lciafmt.get_method(method, endpoint = True, 
                                       summary = apply_summary)
    data = data.append(data_endpoint, ignore_index = True)
    
    # make flowables case insensitive to handle lack of consistent structure in source file
    data['Flowable'] = data['Flowable'].str.lower()
    
    # map the flows to the Fed.LCA commons flows
    # set preserve_unmapped=True if you want to keep unmapped
    # flows in the resulting data frame
    mapping = method.get_metadata()['mapping']
    mapped_data = lciafmt.map_flows(data, system=mapping, case_insensitive=True)
    
    # write the result to parquet and JSON-LD
    store_method(mapped_data, method)
    for m in mapped_data['Method'].unique():
        save_json(method, mapped_data, m)

if __name__ == "__main__":
    main()
