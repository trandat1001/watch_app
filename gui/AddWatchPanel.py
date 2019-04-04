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
## Class AddWatchPanel
###########################################################################

class AddWatchPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 591,301 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Add New Watch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer13.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer14.Add( self.m_staticText12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_txtName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_txtName, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Brand", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer141.Add( self.m_staticText121, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_cboBrandChoices = []
		self.m_cboBrand = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_cboBrandChoices, wx.CB_READONLY )
		bSizer141.Add( self.m_cboBrand, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer141, 0, wx.EXPAND, 5 )

		bSizer142 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"Material", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText122.Wrap( -1 )

		bSizer142.Add( self.m_staticText122, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_cboMaterialChoices = []
		self.m_cboMaterial = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_cboMaterialChoices, wx.CB_READONLY )
		bSizer142.Add( self.m_cboMaterial, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer142, 0, wx.EXPAND, 5 )

		bSizer1421 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1221 = wx.StaticText( self, wx.ID_ANY, u"Movement", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_staticText1221.Wrap( -1 )

		bSizer1421.Add( self.m_staticText1221, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_cboMovementChoices = []
		self.m_cboMovement = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_cboMovementChoices, wx.CB_READONLY )
		bSizer1421.Add( self.m_cboMovement, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer1421, 0, wx.EXPAND, 5 )

		bSizer14211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14211.Add( self.m_btnSave, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14211.Add( self.m_btnCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer14211, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_error = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_error.Wrap( -1 )

		self.m_error.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer13.Add( self.m_error, 0, wx.ALL|wx.EXPAND, 5 )

		
		self.SetSizer( bSizer13 )
		self.Layout()

		# Connect Events
		self.m_btnSave.Bind( wx.EVT_BUTTON, self.m_btnSave_click )
		self.m_btnCancel.Bind( wx.EVT_BUTTON, self.m_btnCancel_click )
		self.initData()

	def __del__( self ):
		pass

	def initData(self):
    	# Empty name
		self.m_txtName.SetValue("")	
    	# Load data for m_cboBand
		brands = DBConnection.fetchAll("SELECT * FROM tb_brand")
		for item in brands:
			self.m_cboBrand.Append(item[1], item[0])
		self.m_cboBrand.SetSelection(0)
		# Load data for m_cboBand
		material = DBConnection.fetchAll("SELECT * FROM tb_material")
		for item in material:
			self.m_cboMaterial.Append(item[1], item[0])
		self.m_cboMaterial.SetSelection(0)
		# Load data for m_cboMovement
		movement = DBConnection.fetchAll("SELECT * FROM tb_movement")
		for item in movement:
			self.m_cboMovement.Append(item[1], item[0])
		self.m_cboMovement.SetSelection(0)

		return 

	# Virtual event handlers, overide them in your derived class
	def m_btnSave_click( self, event ):
		name = self.m_txtName.GetValue()
		brandId = self.m_cboBrand.GetClientData(self.m_cboBrand.GetSelection())
		materialId = self.m_cboMaterial.GetClientData(self.m_cboMaterial.GetSelection())
		movementId = self.m_cboMovement.GetClientData(self.m_cboMovement.GetSelection())
		DBConnection.execute("INSERT INTO tb_watch(name, brand_id, material_id, movement_id) " +
							"VALUES(:_name, :_brand_id, :_material_id, :_movement_id)", 
							{"_name": name, "_brand_id": brandId, "_material_id": materialId, "_movement_id": movementId})
		if (DBConnection.commit() is None):
			wx.MessageBox("New Watch has been saved successfully", "Information", wx.OK)
			self.initData()
		else:
			wx.MessageBox("There is an error. Contact Admin for further information", "Information", wx.OK)	

	def m_btnCancel_click( self, event ):
		self.Parent.Close(True)

		return


