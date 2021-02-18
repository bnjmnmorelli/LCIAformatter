import logging as log
import os

import lciafmt
from lciafmt.util import outputpath, store_method

mod = None

method = lciafmt.Method.ImpactWorld

#To obtain LCIA endpoint categories (damage assessment) set to True
endpoint = False

def main():
    os.makedirs(outputpath, exist_ok=True)
    log.basicConfig(level=log.INFO)

    file = method.get_filename()

    data = lciafmt.get_method(method, endpoint = endpoint)

    # Ben Y. I commented off this code block thinking that it is not necessary.
    # if mod is not None:
       # log.info("getting modified CFs")
       # modified_cfs = lciafmt.get_modification(mod, "ImpactWorld")
       # data = data.merge(modified_cfs, how='left', on=['Flowable', 'Context', 'Indicator'])
       # data.loc[data['Updated CF'].notnull(), 'Characterization Factor'] = data['Updated CF']
       # data = data.drop(columns=['Updated CF', 'Note'])
       # data['Method'] = "ImpactWorld (" + mod + " mod)"

    # map the flows to the Fed.LCA commons flows
    # set preserve_unmapped=True if you want to keep unmapped
    # flows in the resulting data frame
    mapping = method.get_metadata()['mapping']
    mapped_data = lciafmt.map_flows(data, system=mapping)

    # write the result to parquet and JSON-LD
    store_method(mapped_data, method)

    # Ben Y. I commented off this code block thinking that it is not necessary.
    # if mod is not None:
    #    file = mod + "_" + file
    if endpoint:
        json_pack = outputpath + file + "_endpoint_json.zip"
    else:
        json_pack = outputpath + file + "_json.zip"
    if os.path.exists(json_pack):
        os.remove(json_pack)
    lciafmt.to_jsonld(mapped_data, json_pack)


if __name__ == "__main__":
    main()
