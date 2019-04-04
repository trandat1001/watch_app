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
## Class BrandPanel
###########################################################################

class BrandPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Brand Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_txtBrandName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_txtBrandName, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnAdd = wx.Button( self, wx.ID_ANY, u"&Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_btnAdd, 0, wx.ALL, 5 )

		self.m_btnUpdate = wx.Button( self, wx.ID_ANY, u"&Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnUpdate.Enable( False )

		bSizer2.Add( self.m_btnUpdate, 0, wx.ALL, 5 )

		self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"&Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnDelete.Enable( False )

		bSizer2.Add( self.m_btnDelete, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_lstBrandChoices = []
		self.m_lstBrand = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstBrandChoices, 0 )
		bSizer1.Add( self.m_lstBrand, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnAdd.Bind( wx.EVT_BUTTON, self.m_btnAdd_click )
		self.m_btnUpdate.Bind( wx.EVT_BUTTON, self.m_btnUpdate_click )
		self.m_btnDelete.Bind( wx.EVT_BUTTON, self.m_btnDelete_click )
		self.m_lstBrand.Bind( wx.EVT_LISTBOX, self.m_lstBrand_click )

		self.initData()
	def __del__( self ):
		pass

	def initData(self):
		brandList = []
		brands = DBConnection.fetchAll("SELECT * FROM tb_brand ORDER BY name")
		
		for item in brands:
			brandList.append(item[1])
		self.m_lstBrand.AppendItems(brandList)

		return

	# Virtual event handlers, overide them in your derived class
	def m_btnAdd_click( self, event ):
		brandName = self.m_txtBrandName.GetValue().strip()
		if (len(brandName) > 0):
			DBConnection.execute("INSERT INTO tb_brand(name) VALUES(:_name)", {"_name": brandName})
			DBConnection.commit()
			self.m_lstBrand.Append(brandName)
			self.m_txtBrandName.Clear()
		else:
			wx.MessageBox("Please input brand name", "Information", wx.OK)
		
		return

	def m_btnUpdate_click( self, event ):
		updateName = self.m_txtBrandName.GetValue().strip()
		oldName = self.m_lstBrand.GetStringSelection()
		selectIndex = self.m_lstBrand.GetSelection()
		if (len(updateName) > 0):
			sql = '''
				UPDATE tb_brand 
				SET name = :new_name
				WHERE name = :old_name
				'''	
			DBConnection.execute(sql, {"new_name": updateName, "old_name": oldName})
			DBConnection.commit()
			self.m_lstBrand.SetString(selectIndex, updateName)
		else:
			wx.MessageBox("Please input brand name", "Information", wx.OK)
		
		return

	def m_btnDelete_click( self, event ):
		currentName = self.m_lstBrand.GetStringSelection()
		sql = '''
				DELETE FROM tb_brand 
				WHERE name = :name
				'''	
		DBConnection.execute(sql, {"name": currentName})
		DBConnection.commit()
		self.m_lstBrand.Clear()
		self.m_txtBrandName.Clear()
		self.initData()
		
		return

	def m_lstBrand_click( self, event ):
		selectName = self.m_lstBrand.GetStringSelection()
		self.m_txtBrandName.SetValue(selectName)
		self.m_btnUpdate.Enable(True)
		self.m_btnDelete.Enable(True)

		return 


