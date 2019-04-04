# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 27 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from lib.DBConnection import *

###########################################################################
## Class StrapMaterialPanel
###########################################################################

class StrapMaterialPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 537,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Strap Material", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_txtMaterial = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_txtMaterial, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnAdd = wx.Button( self, wx.ID_ANY, u"&Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_btnAdd, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_btnUpdate = wx.Button( self, wx.ID_ANY, u"&Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnUpdate.Enable( False )

		bSizer2.Add( self.m_btnUpdate, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"&Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnDelete.Enable( False )

		bSizer2.Add( self.m_btnDelete, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_lstMaterialChoices = []
		self.m_lstMaterial = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstMaterialChoices, 0 )
		bSizer1.Add( self.m_lstMaterial, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnAdd.Bind( wx.EVT_BUTTON, self.m_btnAdd_click )
		self.m_btnUpdate.Bind( wx.EVT_BUTTON, self.m_btnUpdate_click )
		self.m_btnDelete.Bind( wx.EVT_BUTTON, self.m_btnDelete_click )
		self.m_lstMaterial.Bind( wx.EVT_LISTBOX, self.m_lstMaterial_click )
		self.initData()

	def __del__( self ):
		pass

	def initData(self):
		listMaterial = []
		material = DBConnection.fetchAll("SELECT * FROM tb_material ORDER BY name")
		
		for item in material:
			listMaterial.append(item[1])
		self.m_lstMaterial.AppendItems(listMaterial)

	# Virtual event handlers, overide them in your derived class
	def m_btnAdd_click( self, event ):
		newName = self.m_txtMaterial.GetValue().strip()
		if (len(newName) > 0):
			DBConnection.execute("INSERT INTO tb_material(name) VALUES(:_name)", {"_name": newName})
			DBConnection.commit()
			self.m_lstMaterial.Append(newName)
			self.m_txtMaterial.Clear()
		else:
			wx.MessageBox("Please input material", "Information", wx.OK)
		
		return

	def m_btnUpdate_click( self, event ):
		updateName = self.m_txtMaterial.GetValue().strip()
		currentName = self.m_lstMaterial.GetStringSelection()
		selectIndex = self.m_lstMaterial.GetSelection()
		if (len(updateName) > 0):
			sql = '''
				UPDATE tb_material 
				SET name = :new_name
				WHERE name = :old_name
				'''	
			DBConnection.execute(sql, {"new_name": updateName, "old_name": currentName})
			DBConnection.commit()
			self.m_lstMaterial.SetString(selectIndex, updateName)
		else:
			wx.MessageBox("Please input material", "Information", wx.OK)
		
		return

	def m_btnDelete_click( self, event ):
		currentName = self.m_lstMaterial.GetStringSelection()
		sql = '''
				DELETE FROM tb_material 
				WHERE name = :current_name
				'''	
		DBConnection.execute(sql, {"current_name": currentName})
		DBConnection.commit()
		self.m_lstMaterial.Clear()
		self.m_txtMaterial.Clear()
		self.initData()
		
		return

	def m_lstMaterial_click( self, event ):
		selectName = self.m_lstMaterial.GetStringSelection()
		self.m_txtMaterial.SetValue(selectName)
		self.m_btnUpdate.Enable(True)
		self.m_btnDelete.Enable(True)

		return 


