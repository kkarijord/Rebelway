import hou

def get_assets():
    default_dir= hou.text.expandString('$RBW')
    print(default_dir)
    select_dir= hou.ui.selectFile(
        start_directory=default_dir,
            title='Select the file you want to import',
            file_type=hou.fileType.Geometry, multiple_select=True
    )


    set_specific_scale = hou.ui.displayCustomConfirmation(
        'Do you want to change scale?', buttons= ('Yes', 'No')
    )

    if not set_specific_scale:
        set_scale = hou.ui.readInput(
            'Set scale value for assets', buttons= ('OK', 'Cancel')
        )[1]

    else:
        set_scale = 1

    #Create list with selected directories
    select_dir = select_dir.split(';')

    #Create node
    obj = hou.node("obj")
    geo_node = obj.createNode('geo',node_name='tempGeo')

    merge_node = geo_node.createNode('merge', node_name= 'merge_ALL')
    nodes_to_merge = []
    for num, item in enumerate(select_dir):
        item = item.strip()
        asset_name = item.split('/')[-1]
        asset_name_lst = asset_name.split('.')

        if asset_name_lst[1] == 'abc':
            alembic_node = geo_node.createNode('alembic', node_name= asset_name_lst[0])
            alembic_node.parm('fileName').set(item)
            alembic_node.setColor(hou.Color((1,1,1))) #set color
            end_node = geo_node.createNode('unpack')
            end_node.setInput(0,alembic_node)

        else:
            end_node = geo_node.createNode('file', node_name= asset_name_lst[0])
            end_node.parm('file').set(item)

        #scale connected to input geometry
        transform_node = geo_node.createNode('xform', node_name = f'{asset_name_lst[0]}_xform')
        transform_node.parm('scale').set(set_scale)
        transform_node.setInput(0,end_node)

        #assign material nodes to transform
        material_node = geo_node.createNode('material',node_name= f'{asset_name_lst[0]}_mat')
        material_node.setInput(0,transform_node)
        
        nodes_to_merge.append(material_node)
        
    for num, node in enumerate(nodes_to_merge):
        merge_node.setInput(num,node)
        merge_node.setDisplayFlag(True)

    geo_node.layoutChildren() # Layout the nodes created

    