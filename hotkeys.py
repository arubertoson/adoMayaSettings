# hotkey, [name, command, args]
HOTKEYS = {
    # Selection masks
    '1': ['select_mask_vertex', 'ahelper.set_component_mask("POINT")'],
    '2': ['select_mask_edge', 'ahelper.set_component_mask("EDGE")'],
    '3': ['select_mask_face', 'ahelper.set_component_mask("FACE")'],
    '4': ['select_mask_map', 'ahelper.set_component_mask("MAP")'],
    '5': ['select_mask_object', 'ahelper.set_object_mask()'],

    # Select
    'alt+1': ['convert_to_vertex', 'aselect.Convert().to_vertex()'],
    'alt+2': ['convert_to_edge', 'aselect.Convert().to_edge()'],
    'alt+3': ['convert_to_face', 'aselect.Convert().to_face()'],
    'alt+4': ['convert_to_map', 'aselect.Convert().to_map()'],

    'alt+!': ['convert_to_bvertex', 'aselect.Convert(border=True).to_vertex()'],
    'alt+@': ['convert_to_bedge', 'aselect.Convert(border=True).to_edge()'],
    'alt+#': ['convert_to_bface', 'aselect.Convert(border=True).to_face()'],
    'alt+$': ['convert_to_bmap', 'aselect.Convert(border=True).to_map()'],

    'ctrl+alt+Up': ['select_pattern_next', 'aselect.pattern_next()'],
    'ctrl+alt+Down': ['select_pattern_previous', 'aselect.pattern_previous()'],
    'Q': ['select_deselect_all', 'aselect.clear()'],

    # Tools
    'alt+e': ['tool_extrude', 'atoolsModel.extrude()'],
    'ctrl+b': ['tool_bridge', 'atoolsModel.bridge()'],

    # Window toggles
    '6': ['window_outliner', 'atoggleWindows.outliner()'],
    '7': ['window_hypershader', 'atoggleWindows.hypershader()'],
    '8': ['window_scripteditor', 'atoggleWindows.scripteditor()'],
    '9': ['window_renderview', 'atoggleWindows.renderview()'],

    # Pie menus
    'alt+d': ['PMdelete', 'aprefPieMenus.delete_pie()'],
    'alt+q': ['PMselect', 'aprefPieMenus.select_pie()'],

    'W': ['PMmodel', 'aprefPieMenus.model_pie()'],
    'A': ['PMpivot', 'aprefPieMenus.pivot_pie()'],
    'alt+a': ['PMalignUV', 'aprefPieMenus.align_uv()'],
    'X': ['PMuv', 'aprefPieMenus.uv_pie()'],

    'alt+W': ['PMmirror', 'aprefPieMenus.poly_mirror_pie()'],
    'E': ['PMduplicateDetach', 'aprefPieMenus.duplicate_detach_pie()'],

    'ctrl+F': ['PMcamera', 'aprefPieMenus.camera_pie()'],
    'alt+w': ['PMdisplay', 'aprefPieMenus.display_pie()'],
    'ctrl+e': ['PMnormals', 'aprefPieMenus.poly_normal_pie()'],


    # Camera / display
    'H': ['isolate_selected', 'atoggleDisplay.isolate_selected()'],
    'h': ['hide_selected', 'atoggleDisplay.hide_selected()'],
    'u': ['unhide_all', 'atoggleDisplay.unhide_all()'],
    'F': ['camera_viewport_snap', 'acamera.viewport_snap()'],
    'ctrl+alt+f': ['camera_fit_last', 'acamera.Camera().fit_selection()'],


    # SubD Toggles
    'F1': ['SubD_toggle', 'atoggleSubD.toggle(True)'],
    'ctrl+F1': ['SubD_all_off', 'atoggleSubD.all_off()'],
    'ctrl++': ['SubD_add_level', 'atoggleSubD.add_level()'],
    'ctrl+-': ['SubD_sub_level', 'atoggleSubD.sub_level()'],

    # Various
    'F2': ['Renamer', 'arenamer.Renamer().run()']

}
