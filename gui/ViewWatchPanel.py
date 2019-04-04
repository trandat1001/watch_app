# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 27 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
from lib.DBConnection import *

###########################################################################
## Class ViewWatchPanel
###########################################################################

class ViewWatchPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Watch", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_gridWatch = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_gridWatch.CreateGrid( 0, 5 )
		self.m_gridWatch.EnableEditing( False )
		self.m_gridWatch.EnableGridLines( True )
		self.m_gridWatch.EnableDragGridSize( False )
		self.m_gridWatch.SetMargins( 0, 0 )

		# Columns
		self.m_gridWatch.SetColSize( 0, 200 )
		self.m_gridWatch.SetColSize( 1, 200 )
		self.m_gridWatch.SetColSize( 2, 200 )
		self.m_gridWatch.SetColSize( 3, 200 )
		self.m_gridWatch.SetColSize( 4, 200 )
		self.m_gridWatch.EnableDragColMove( False )
		self.m_gridWatch.EnableDragColSize( True )
		self.m_gridWatch.SetColLabelSize( 30 )
		self.m_gridWatch.SetColLabelValue( 0, u"Id" )		
		self.m_gridWatch.SetColLabelValue( 1, u"Name" )
		self.m_gridWatch.SetColLabelValue( 2, u"Brand" )
		self.m_gridWatch.SetColLabelValue( 3, u"Movement" )
		self.m_gridWatch.SetColLabelValue( 4, u"Material" )
		self.m_gridWatch.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_gridWatch.EnableDragRowSize( True )
		self.m_gridWatch.SetRowLabelSize( 80 )
		self.m_gridWatch.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_gridWatch.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.m_gridWatch, 1, wx.ALL|wx.EXPAND, 5 )
		# Connect Events
		#self.m_gridWatch.Bind( wx.grid.EVT_GRID_CELL_CHANGING, self.gird_row_edit )

		self.SetSizer( bSizer17 )
		self.Layout()
		self.initData()

	def __del__( self ):
		pass

	def initData(self):
		watches = DBConnection.fetchAll('	SELECT tb_watch.id, tb_watch.name, tb_brand.name as "brand", tb_material.name as "material", tb_movement.name as "movement" '
											'FROM tb_watch JOIN tb_brand '
											'ON tb_watch.brand_id = tb_brand.id '
											'JOIN tb_material ' 
											'ON tb_watch.material_id = tb_material.id '
											'JOIN tb_movement '
											'ON tb_watch.movement_id = tb_movement.id'
										)
		print(watches)
		self.m_gridWatch.AppendRows(len(watches))
		for index in range(len(watches)):
			self.m_gridWatch.SetCellValue(index, 0, str(watches[index][0]))
			self.m_gridWatch.SetCellValue(index, 1, str(watches[index][1]))
			self.m_gridWatch.SetCellValue(index, 2, str(watches[index][2]))
			self.m_gridWatch.SetCellValue(index, 3, str(watches[index][3]))
			self.m_gridWatch.SetCellValue(index, 4, str(watches[index][4]))
		self.m_gridWatch.HideCol(0)
		
	# Virtual event handlers, overide them in your derived class
	def gird_row_edit( self, event ):
		print(event.GetString())
		rowIndex = event.GetRow()
		self.m_gridWatch.GetCellValue(rowIndex, 0)
		id = self.m_gridWatch.GetCellValue(rowIndex, 0)
		print(id)
		self.m_gridWatch.GetCellValue(rowIndex, 1)
		self.m_gridWatch.GetCellValue(rowIndex, 3)



