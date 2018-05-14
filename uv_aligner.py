# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Magenta UV Aligner",
    "author": "Thiago Kuhn",
    "version": (0, 1),
    "blender": (2, 7, 9),
    "location": "UV/Image Editor > Tool Shelf > Align",
    "description": "Aligns selected UVs to Left, Right, Up or Down, taking in account the selected UVs",
    "category": "UV"
}

import bpy
import math

class AlignLeft(bpy.types.Operator):
    bl_idname = "uv.align_left"
    bl_label = "Align Left"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        # UV data is accessible only in object mode
        prev_mode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Update vertex selection properties, in case the script wasn't run in
        # object mode
        bpy.context.object.update_from_editmode()
        
        # If the object is not a mesh, the script does not continue
        if (bpy.context.object.type != 'MESH'):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The selected object is not mesh.')
            return {'CANCELLED'}
        
        # If the mesh has no UV layers, the script does not continue
        mesh = bpy.context.object.data
        if not (mesh.uv_layers):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The mesh must have an UV Map.')
            return {'CANCELLED'}
        
        # If the option 'sync selection' is selected, the script does not continue
        if bpy.context.scene.tool_settings.use_uv_select_sync:
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The button "sync selection" must be disabled.')
            return {'CANCELLED'}

        uv_map = mesh.uv_layers.active
        selected_uvs = []

        for index, uv_loop in enumerate(uv_map.data):
            if(uv_loop.select):
                selected_uvs.append(uv_map.data[index])
        
        # If there are less than 2 UVs selected, the script does not continue
        if (len(selected_uvs) < 2):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'You must select at least two UV coordinates.')
            return {'CANCELLED'}

        # Defines the value to be used by the UVs, by iterating all the UVs and getting the smaller/bigger value
        value = math.inf
        for current_uv in selected_uvs:
            if (current_uv.uv.x < value):
                value = current_uv.uv.x

        # Applies the value to all the UVs
        for current_uv in selected_uvs:
            current_uv.uv.x = value

        # Restore whatever mode the object is in previously
        bpy.ops.object.mode_set(mode=prev_mode)
        return {'FINISHED'}

class AlignRight(bpy.types.Operator):
    bl_idname = "uv.align_right"
    bl_label = "Align Right"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        # UV data is accessible only in object mode
        prev_mode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Update vertex selection properties, in case the script wasn't run in
        # object mode
        bpy.context.object.update_from_editmode()
        
        # If the object is not a mesh, the script does not continue
        if (bpy.context.object.type != 'MESH'):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The selected object is not mesh.')
            return {'CANCELLED'}
        
        # If the mesh has no UV layers, the script does not continue
        mesh = bpy.context.object.data
        if not (mesh.uv_layers):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The mesh must have an UV Map.')
            return {'CANCELLED'}
        
        # If the option 'sync selection' is selected, the script does not continue
        if bpy.context.scene.tool_settings.use_uv_select_sync:
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The button "sync selection" must be disabled.')
            return {'CANCELLED'}

        uv_map = mesh.uv_layers.active
        selected_uvs = []

        for index, uv_loop in enumerate(uv_map.data):
            if(uv_loop.select):
                selected_uvs.append(uv_map.data[index])
        
        # If there are less than 2 UVs selected, the script does not continue
        if (len(selected_uvs) < 2):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'You must select at least two UV coordinates.')
            return {'CANCELLED'}

        # Defines the value to be used by the UVs, by iterating all the UVs and getting the smaller/bigger value
        value = -math.inf
        for current_uv in selected_uvs:
            if (current_uv.uv.x > value):
                value = current_uv.uv.x

        # Applies the value to all the UVs
        for current_uv in selected_uvs:
            current_uv.uv.x = value

        # Restore whatever mode the object is in previously
        bpy.ops.object.mode_set(mode=prev_mode)
        return {'FINISHED'}

class AlignUp(bpy.types.Operator):
    bl_idname = "uv.align_up"
    bl_label = "Align Up"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        # UV data is accessible only in object mode
        prev_mode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Update vertex selection properties, in case the script wasn't run in
        # object mode
        bpy.context.object.update_from_editmode()
        
        # If the object is not a mesh, the script does not continue
        if (bpy.context.object.type != 'MESH'):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The selected object is not mesh.')
            return {'CANCELLED'}
        
        # If the mesh has no UV layers, the script does not continue
        mesh = bpy.context.object.data
        if not (mesh.uv_layers):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The mesh must have an UV Map.')
            return {'CANCELLED'}
        
        # If the option 'sync selection' is selected, the script does not continue
        if bpy.context.scene.tool_settings.use_uv_select_sync:
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The button "sync selection" must be disabled.')
            return {'CANCELLED'}

        uv_map = mesh.uv_layers.active
        selected_uvs = []

        for index, uv_loop in enumerate(uv_map.data):
            if(uv_loop.select):
                selected_uvs.append(uv_map.data[index])
        
        # If there are less than 2 UVs selected, the script does not continue
        if (len(selected_uvs) < 2):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'You must select at least two UV coordinates.')
            return {'CANCELLED'}

        # Defines the value to be used by the UVs, by iterating all the UVs and getting the smaller/bigger value
        value = -math.inf
        for current_uv in selected_uvs:
            if (current_uv.uv.y > value):
                value = current_uv.uv.y

        # Applies the value to all the UVs
        for current_uv in selected_uvs:
            current_uv.uv.y = value

        # Restore whatever mode the object is in previously
        bpy.ops.object.mode_set(mode=prev_mode)
        return {'FINISHED'}

class AlignDown(bpy.types.Operator):
    bl_idname = "uv.align_down"
    bl_label = "Align Down"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        # UV data is accessible only in object mode
        prev_mode = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')

        # Update vertex selection properties, in case the script wasn't run in
        # object mode
        bpy.context.object.update_from_editmode()
        
        # If the object is not a mesh, the script does not continue
        if (bpy.context.object.type != 'MESH'):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The selected object is not mesh.')
            return {'CANCELLED'}
        
        # If the mesh has no UV layers, the script does not continue
        mesh = bpy.context.object.data
        if not (mesh.uv_layers):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The mesh must have an UV Map.')
            return {'CANCELLED'}
        
        # If the option 'sync selection' is selected, the script does not continue
        if bpy.context.scene.tool_settings.use_uv_select_sync:
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'The button "sync selection" must be disabled.')
            return {'CANCELLED'}

        uv_map = mesh.uv_layers.active
        selected_uvs = []

        for index, uv_loop in enumerate(uv_map.data):
            if(uv_loop.select):
                selected_uvs.append(uv_map.data[index])
        
        # If there are less than 2 UVs selected, the script does not continue
        if (len(selected_uvs) < 2):
            bpy.ops.object.mode_set(mode=prev_mode)
            self.report({'ERROR'}, 'You must select at least two UV coordinates.')
            return {'CANCELLED'}

        # Defines the value to be used by the UVs, by iterating all the UVs and getting the smaller/bigger value
        value = math.inf
        for current_uv in selected_uvs:
            if (current_uv.uv.y < value):
                value = current_uv.uv.y

        # Applies the value to all the UVs
        for current_uv in selected_uvs:
            current_uv.uv.y = value

        # Restore whatever mode the object is in previously
        bpy.ops.object.mode_set(mode=prev_mode)
        return {'FINISHED'}

class UI_Align(bpy.types.Panel):
    bl_label = "Magenta UV Aligner"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "TOOLS"
    bl_category = "Tools"

    def draw(self, context):
        scn = context.scene
        layout = self.layout
		
        row = layout.row(align=True)
        row.operator("uv.align_left", "Align Left")
        row.operator("uv.align_right", "Align Right")
		
        row = layout.row(align=True)
        row.operator("uv.align_up", "Align Up")
        row.operator("uv.align_down", "Align Down")
    
def register():
    bpy.utils.register_class(AlignLeft)
    bpy.utils.register_class(AlignRight)
    bpy.utils.register_class(AlignUp)
    bpy.utils.register_class(AlignDown)
    bpy.utils.register_class(UI_Align)

def unregister():
    bpy.utils.unregister_class(AlignLeft)
    bpy.utils.unregister_class(AlignRight)
    bpy.utils.unregister_class(AlignUp)
    bpy.utils.unregister_class(AlignDown)
    bpy.utils.unregister_class(UI_Align)

if __name__ == "__main__":
    register()