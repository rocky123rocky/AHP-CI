from ahp_backend import import_excel_to_project, load_project
import json
proj='ref_import_test'
side='blue'
import_excel_to_project(proj, side, 'Ref Force new.xlsx')
data=load_project(proj, side)
out=[{'DP No':dp.get('DP No'), 'Name':dp.get('Name'), 'Objective':dp.get('Objective'),'Phase':dp.get('Phase'),'Force Group':dp.get('Force Group')} for dp in data.get('dps',[])][:10]
print(json.dumps(out, indent=2))
