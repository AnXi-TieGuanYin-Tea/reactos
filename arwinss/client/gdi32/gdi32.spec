@ stdcall AbortDoc(long)
@ stdcall AbortPath(long)
@ stdcall AddFontMemResourceEx(ptr long ptr ptr)
@ stdcall AddFontResourceA(str)
@ stdcall AddFontResourceExA(str long ptr)
@ stdcall AddFontResourceExW(wstr long ptr)
@ stub AddFontResourceTracking
@ stdcall AddFontResourceW(wstr)
@ stdcall AngleArc(long long long long long long)
@ stdcall AnimatePalette(long long long ptr)
@ stub AnyLinkedFonts
@ stdcall Arc(long long long long long long long long long)
@ stdcall ArcTo(long long long long long long long long long)
@ stub BRUSHOBJ_hGetColorTransform
@ stub BRUSHOBJ_pvAllocRbrush
@ stub BRUSHOBJ_pvGetRbrush
@ stub BRUSHOBJ_ulGetBrushColor
@ stdcall BeginPath(long)
@ stdcall BitBlt(long long long long long long long long long)
@ stub ByeByeGDI
@ stub CLIPOBJ_bEnum
@ stub CLIPOBJ_cEnumStart
@ stub CLIPOBJ_ppoGetPath
@ stdcall CancelDC(long)
@ stub CheckColorsInGamut
@ stdcall ChoosePixelFormat(long ptr)
@ stdcall Chord(long long long long long long long long long)
@ stub ClearBitmapAttributes
@ stub ClearBrushAttributes
@ stdcall CloseEnhMetaFile(long)
@ stdcall CloseFigure(long)
@ stdcall CloseMetaFile(long)
@ stub ColorCorrectPalette
@ stub ColorMatchToTarget
@ stdcall CombineRgn(long long long long)
@ stdcall CombineTransform(ptr ptr ptr)
@ stdcall CopyEnhMetaFileA(long str)
@ stdcall CopyEnhMetaFileW(long wstr)
@ stdcall CopyMetaFileA(long str)
@ stdcall CopyMetaFileW(long wstr)
@ stdcall CreateBitmap(long long long long ptr)
@ stdcall CreateBitmapIndirect(ptr)
@ stdcall CreateBrushIndirect(ptr)
@ stdcall CreateColorSpaceA(ptr)
@ stdcall CreateColorSpaceW(ptr)
@ stdcall CreateCompatibleBitmap(long long long)
@ stdcall CreateCompatibleDC(long)
@ stdcall CreateDCA(str str str ptr)
@ stdcall CreateDCW(wstr wstr wstr ptr)
@ stdcall CreateDIBPatternBrush(long long)
@ stdcall CreateDIBPatternBrushPt(long long)
@ stdcall CreateDIBSection(long ptr long ptr long long)
@ stdcall CreateDIBitmap(long ptr long ptr ptr long)
@ stdcall CreateDiscardableBitmap(long long long)
@ stdcall CreateEllipticRgn(long long long long)
@ stdcall CreateEllipticRgnIndirect(ptr)
@ stdcall CreateEnhMetaFileA(long str ptr str)
@ stdcall CreateEnhMetaFileW(long wstr ptr wstr)
@ stdcall CreateFontA(long long long long long long long long long long long long long str)
@ stdcall CreateFontIndirectA(ptr)
@ stdcall CreateFontIndirectExA(ptr)
@ stdcall CreateFontIndirectExW(ptr)
@ stdcall CreateFontIndirectW(ptr)
@ stdcall CreateFontW(long long long long long long long long long long long long long wstr)
@ stdcall CreateHalftonePalette(long)
@ stdcall CreateHatchBrush(long long)
@ stdcall CreateICA(str str str ptr)
@ stdcall CreateICW(wstr wstr wstr ptr)
@ stdcall CreateMetaFileA(str)
@ stdcall CreateMetaFileW(wstr)
@ stdcall CreatePalette(ptr)
@ stdcall CreatePatternBrush(long)
@ stdcall CreatePen(long long long)
@ stdcall CreatePenIndirect(ptr)
@ stdcall CreatePolyPolygonRgn(ptr ptr long long)
@ stdcall CreatePolygonRgn(ptr long long)
@ stdcall CreateRectRgn(long long long long)
@ stdcall CreateRectRgnIndirect(ptr)
@ stdcall CreateRoundRectRgn(long long long long long long)
@ stdcall CreateScalableFontResourceA(long str str str)
@ stdcall CreateScalableFontResourceW(long wstr wstr wstr)
@ stdcall CreateSolidBrush(long)
@ stdcall DPtoLP(long ptr long)
@ stub DdEntry0
@ stub DdEntry10
@ stub DdEntry11
@ stub DdEntry12
@ stub DdEntry13
@ stub DdEntry14
@ stub DdEntry15
@ stub DdEntry16
@ stub DdEntry17
@ stub DdEntry18
@ stub DdEntry19
@ stub DdEntry1
@ stub DdEntry20
@ stub DdEntry21
@ stub DdEntry22
@ stub DdEntry23
@ stub DdEntry24
@ stub DdEntry25
@ stub DdEntry26
@ stub DdEntry27
@ stub DdEntry28
@ stub DdEntry29
@ stub DdEntry2
@ stub DdEntry30
@ stub DdEntry31
@ stub DdEntry32
@ stub DdEntry33
@ stub DdEntry34
@ stub DdEntry35
@ stub DdEntry36
@ stub DdEntry37
@ stub DdEntry38
@ stub DdEntry39
@ stub DdEntry3
@ stub DdEntry40
@ stub DdEntry41
@ stub DdEntry42
@ stub DdEntry43
@ stub DdEntry44
@ stub DdEntry45
@ stub DdEntry46
@ stub DdEntry47
@ stub DdEntry48
@ stub DdEntry49
@ stub DdEntry4
@ stub DdEntry50
@ stub DdEntry51
@ stub DdEntry52
@ stub DdEntry53
@ stub DdEntry54
@ stub DdEntry55
@ stub DdEntry56
@ stub DdEntry5
@ stub DdEntry6
@ stub DdEntry7
@ stub DdEntry8
@ stub DdEntry9
@ stdcall DeleteColorSpace(long)
@ stdcall DeleteDC(long)
@ stdcall DeleteEnhMetaFile(long)
@ stdcall DeleteMetaFile(long)
@ stdcall DeleteObject(long)
@ stdcall DescribePixelFormat(long long long ptr)
@ stub DeviceCapabilitiesEx
@ stub DeviceCapabilitiesExA
@ stub DeviceCapabilitiesExW
@ stdcall DrawEscape(long long long ptr)
@ stdcall Ellipse(long long long long long)
@ stdcall EnableEUDC(long)
@ stdcall EndDoc(long)
@ stub EndFormPage
@ stdcall EndPage(long)
@ stdcall EndPath(long)
@ stdcall EngAcquireSemaphore(ptr)
@ stub EngAlphaBlend
@ stub EngAssociateSurface
@ stub EngBitBlt
@ stub EngCheckAbort
@ stub EngComputeGlyphSet
@ stub EngCopyBits
@ stub EngCreateBitmap
@ stub EngCreateClip
@ stub EngCreateDeviceBitmap
@ stub EngCreateDeviceSurface
@ stub EngCreatePalette
@ stdcall EngCreateSemaphore()
@ stub EngDeleteClip
@ stub EngDeletePalette
@ stub EngDeletePath
@ stdcall EngDeleteSemaphore(ptr)
@ stub EngDeleteSurface
@ stub EngEraseSurface
@ stub EngFillPath
@ stdcall EngFindResource(ptr long long ptr)
@ stdcall EngFreeModule(ptr)
@ stdcall EngGetCurrentCodePage(ptr ptr)
@ stub EngGetDriverName
@ stub EngGetPrinterDataFileName
@ stub EngGradientFill
@ stub EngLineTo
@ stdcall EngLoadModule(ptr)
@ stub EngLockSurface
@ stub EngMarkBandingSurface
@ stub EngMultiByteToUnicodeN
@ stdcall EngMultiByteToWideChar(long wstr long str long)
@ stub EngPaint
@ stub EngPlgBlt
@ stub EngQueryEMFInfo
@ stdcall EngQueryLocalTime(ptr)
@ stdcall EngReleaseSemaphore(ptr)
@ stub EngStretchBlt
@ stub EngStretchBltROP
@ stub EngStrokeAndFillPath
@ stub EngStrokePath
@ stub EngTextOut
@ stub EngTransparentBlt
@ stub EngUnicodeToMultiByteN
@ stub EngUnlockSurface
@ stub EngWideCharToMultiByte
@ stdcall EnumEnhMetaFile(long long ptr ptr ptr)
@ stdcall EnumFontFamiliesA(long str ptr long)
@ stdcall EnumFontFamiliesExA(long ptr ptr long long)
@ stdcall EnumFontFamiliesExW(long ptr ptr long long)
@ stdcall EnumFontFamiliesW(long wstr ptr long)
@ stdcall EnumFontsA(long str ptr long)
@ stdcall EnumFontsW(long wstr ptr long)
@ stdcall EnumICMProfilesA(long ptr long)
@ stdcall EnumICMProfilesW(long ptr long)
@ stdcall EnumMetaFile(long long ptr ptr)
@ stdcall EnumObjects(long long ptr long)
@ stdcall EqualRgn(long long)
@ stdcall Escape(long long long ptr ptr)
@ stub EudcLoadLinkW
@ stub EudcUnloadLinkW
@ stdcall ExcludeClipRect(long long long long long)
@ stdcall ExtCreatePen(long long ptr long ptr)
@ stdcall ExtCreateRegion(ptr long ptr)
@ stdcall ExtEscape(long long long ptr long ptr)
@ stdcall ExtFloodFill(long long long long long)
@ stdcall ExtSelectClipRgn(long long long)
@ stdcall ExtTextOutA(long long long long ptr str long ptr)
@ stdcall ExtTextOutW(long long long long ptr wstr long ptr)
@ stub FONTOBJ_cGetAllGlyphHandles
@ stub FONTOBJ_cGetGlyphs
@ stub FONTOBJ_pQueryGlyphAttrs
@ stub FONTOBJ_pfdg
@ stub FONTOBJ_pifi
@ stub FONTOBJ_pvTrueTypeFontFile
@ stub FONTOBJ_pxoGetXform
@ stub FONTOBJ_vGetInfo
@ stdcall FillPath(long)
@ stdcall FillRgn(long long long)
@ stdcall FixBrushOrgEx(long long long ptr)
@ stdcall FlattenPath(long)
@ stdcall FloodFill(long long long long)
@ stdcall FontIsLinked(long)
@ stdcall FrameRgn(long long long long long)
@ stub FreeImageColorMatcher
@ stdcall GdiAddFontResourceW(ptr ptr ptr)
@ stub GdiAddGlsBounds
@ stub GdiAddGlsRecord
@ stdcall GdiAlphaBlend(long long long long long long long long long long long)
@ stub GdiArtificialDecrementDriver
@ stub GdiAssociateObject
@ stub GdiCleanCacheDC
@ stdcall GdiComment(long long ptr)
@ stub GdiConsoleTextOut
@ stub GdiConvertAndCheckDC
@ stdcall GdiConvertBitmap(ptr)
@ stub GdiConvertBitmapV5
@ stdcall GdiConvertBrush(ptr)
@ stdcall GdiConvertDC(ptr)
@ stub GdiConvertEnhMetaFile
@ stdcall GdiConvertFont(ptr)
@ stub GdiConvertMetaFilePict
@ stdcall GdiConvertPalette(ptr)
@ stdcall GdiConvertRegion(ptr)
@ stdcall GdiConvertToDevmodeW(ptr)
@ stub GdiCreateLocalBitmap
@ stub GdiCreateLocalBrush
@ stub GdiCreateLocalEnhMetaFile
@ stub GdiCreateLocalFont
@ stub GdiCreateLocalMetaFilePict
@ stub GdiCreateLocalPalette
@ stub GdiCreateLocalRegion
@ stub GdiDciBeginAccess
@ stub GdiDciCreateOffscreenSurface
@ stub GdiDciCreateOverlaySurface
@ stub GdiDciCreatePrimarySurface
@ stub GdiDciDestroySurface
@ stub GdiDciDrawSurface
@ stub GdiDciEndAccess
@ stub GdiDciEnumSurface
@ stub GdiDciInitialize
@ stub GdiDciSetClipList
@ stub GdiDciSetDestination
@ stdcall GdiDeleteLocalDC(ptr)
@ stub GdiDeleteLocalObject
@ stub GdiDeleteSpoolFileHandle
@ stdcall GdiDescribePixelFormat(ptr long long ptr)
@ stub GdiDllInitialize
@ stub GdiDrawStream
@ stub GdiEndDocEMF
@ stub GdiEndPageEMF
@ stub GdiEntry10
@ stub GdiEntry11
@ stub GdiEntry12
@ stub GdiEntry13
@ stub GdiEntry14
@ stub GdiEntry15
@ stub GdiEntry16
@ stub GdiEntry1
@ stub GdiEntry2
@ stub GdiEntry3
@ stub GdiEntry4
@ stub GdiEntry5
@ stub GdiEntry6
@ stub GdiEntry7
@ stub GdiEntry8
@ stub GdiEntry9
@ stub GdiFixUpHandle
@ stdcall GdiFlush()
@ stub GdiFullscreenControl
@ stdcall GdiGetBatchLimit()
@ stdcall GdiGetCharDimensions(long ptr ptr)
@ stdcall GdiGetCodePage(long)
@ stub GdiGetDC
@ stub GdiGetDevmodeForPage
@ stub GdiGetLocalBitmap
@ stdcall GdiGetLocalBrush(ptr)
@ stdcall GdiGetLocalDC(ptr)
@ stub GdiGetLocalFont
@ stub GdiGetPageCount
@ stub GdiGetPageHandle
@ stub GdiGetSpoolFileHandle
@ stdcall GdiGetSpoolMessage(ptr long ptr long)
@ stdcall GdiGradientFill(long ptr long ptr long long) 
@ stdcall GdiInitSpool()
@ stdcall GdiInitializeLanguagePack(long)
@ stdcall GdiIsMetaFileDC(long)
@ stdcall GdiIsMetaPrintDC(long)
@ stdcall GdiIsPlayMetafileDC(long)
@ stub GdiPlayDCScript
@ stub GdiPlayEMF
@ stub GdiPlayJournal
@ stub GdiPlayPageEMF
@ stub GdiPlayPrivatePageEMF
@ stub GdiPlayScript
@ stub GdiPrinterThunk
@ stub GdiProcessSetup
@ stub GdiQueryFonts
@ stub GdiQueryTable
@ stdcall GdiRealizationInfo(long ptr)
@ stub GdiReleaseDC
@ stdcall GdiReleaseLocalDC(ptr)
@ stub GdiResetDCEMF
@ stdcall GdiSetAttrs(ptr)
@ stdcall GdiSetBatchLimit(long)
@ stub GdiSetLastError
@ stdcall GdiSetPixelFormat(ptr long)
@ stub GdiSetServerAttr
@ stub GdiStartDocEMF
@ stub GdiStartPageEMF
@ stdcall GdiSwapBuffers(ptr)
@ stdcall GdiTransparentBlt(long long long long long long long long long long long)
@ stub GdiValidateHandle
@ stub GdiWinWatchClose
@ stub GdiWinWatchDidStatusChange
@ stub GdiWinWatchGetClipList
@ stub GdiWinWatchOpen
@ stdcall GetArcDirection(long)
@ stdcall GetAspectRatioFilterEx(long ptr)
@ stub GetBitmapAttributes
@ stdcall GetBitmapBits(long long ptr)
@ stdcall GetBitmapDimensionEx(long ptr)
@ stdcall GetBkColor(long)
@ stdcall GetBkMode(long)
@ stdcall GetBoundsRect(long ptr long)
@ stub GetBrushAttributes
@ stdcall GetBrushOrgEx(long ptr)
@ stdcall GetCharABCWidthsA(long long long ptr)
@ stdcall GetCharABCWidthsFloatA(long long long ptr)
@ stdcall GetCharABCWidthsFloatW(long long long ptr)
@ stdcall GetCharABCWidthsI(long long long ptr ptr)
@ stdcall GetCharABCWidthsW(long long long ptr)
@ stdcall GetCharWidth32A(long long long long)
@ stdcall GetCharWidth32W(long long long long)
@ stdcall GetCharWidthA(long long long long) GetCharWidth32A
@ stdcall GetCharWidthFloatA(long long long ptr)
@ stdcall GetCharWidthFloatW(long long long ptr)
@ stdcall GetCharWidthI(ptr long long ptr ptr)
@ stub GetCharWidthInfo
@ stdcall GetCharWidthW(long long long long) GetCharWidth32W
@ stub GetCharWidthWOW
@ stdcall GetCharacterPlacementA(long str long long ptr long)
@ stdcall GetCharacterPlacementW(long wstr long long ptr long)
@ stdcall GetClipBox(long ptr)
@ stdcall GetClipRgn(long long)
@ stdcall GetColorAdjustment(long ptr)
@ stdcall GetColorSpace(long)
@ stdcall GetCurrentObject(long long)
@ stdcall GetCurrentPositionEx(long ptr)
@ stdcall GetDCBrushColor(long)
@ stdcall GetDCOrgEx(long ptr)
@ stdcall GetDCPenColor(long)
@ stdcall GetDIBColorTable(long long long ptr)
@ stdcall GetDIBits(long long long long ptr ptr long)
@ stdcall GetDeviceCaps(long long)
@ stdcall GetDeviceGammaRamp(long ptr)
@ stub GetETM
@ stub GetEUDCTimeStamp
@ stub GetEUDCTimeStampExW
@ stdcall GetEnhMetaFileA(str)
@ stdcall GetEnhMetaFileBits(long long ptr)
@ stdcall GetEnhMetaFileDescriptionA(long long ptr)
@ stdcall GetEnhMetaFileDescriptionW(long long ptr)
@ stdcall GetEnhMetaFileHeader(long long ptr)
@ stdcall GetEnhMetaFilePaletteEntries (long long ptr)
@ stub GetEnhMetaFilePixelFormat
@ stdcall GetEnhMetaFileW(wstr)
@ stub GetFontAssocStatus
@ stdcall GetFontData(long long long ptr long)
@ stdcall GetFontLanguageInfo(long)
@ stub GetFontResourceInfo
@ stdcall GetFontResourceInfoW(str ptr ptr long)
@ stdcall GetFontUnicodeRanges(ptr ptr)
@ stdcall GetGlyphIndicesA(long ptr long ptr long)
@ stdcall GetGlyphIndicesW(long ptr long ptr long)
@ stdcall GetGlyphOutline(long long long ptr long ptr ptr) GetGlyphOutlineA
@ stdcall GetGlyphOutlineA(long long long ptr long ptr ptr)
@ stdcall GetGlyphOutlineW(long long long ptr long ptr ptr)
@ stub GetGlyphOutlineWow
@ stdcall GetGraphicsMode(long)
@ stub GetHFONT
@ stdcall GetICMProfileA(long ptr ptr)
@ stdcall GetICMProfileW(long ptr ptr)
@ stdcall GetKerningPairs(long long ptr) GetKerningPairsA
@ stdcall GetKerningPairsA(long long ptr)
@ stdcall GetKerningPairsW(long long ptr)
@ stdcall GetLayout(long)
@ stdcall GetLogColorSpaceA(long ptr long)
@ stdcall GetLogColorSpaceW(long ptr long)
@ stdcall GetMapMode(long)
@ stdcall GetMetaFileA(str)
@ stdcall GetMetaFileBitsEx(long long ptr)
@ stdcall GetMetaFileW(wstr)
@ stdcall GetMetaRgn(long long)
@ stdcall GetMiterLimit(long ptr)
@ stdcall GetNearestColor(long long)
@ stdcall GetNearestPaletteIndex(long long)
@ stdcall GetObjectA(long long ptr)
@ stdcall GetObjectType(long)
@ stdcall GetObjectW(long long ptr)
@ stdcall GetOutlineTextMetricsA(long long ptr)
@ stdcall GetOutlineTextMetricsW(long long ptr)
@ stdcall GetPaletteEntries(long long long ptr)
@ stdcall GetPath(long ptr ptr long)
@ stdcall GetPixel(long long long)
@ stdcall GetPixelFormat(long)
@ stdcall GetPolyFillMode(long)
@ stdcall GetROP2(long)
@ stdcall GetRandomRgn(long long long)
@ stdcall GetRasterizerCaps(ptr long)
@ stdcall GetRegionData(long long ptr)
@ stdcall GetRelAbs(long long)
@ stdcall GetRgnBox(long ptr)
@ stdcall GetStockObject(long)
@ stdcall GetStretchBltMode(long)
@ stub GetStringBitmapA
@ stub GetStringBitmapW
@ stdcall GetSystemPaletteEntries(long long long ptr)
@ stdcall GetSystemPaletteUse(long)
@ stdcall GetTextAlign(long)
@ stdcall GetTextCharacterExtra(long)
@ stdcall GetTextCharset(long)
@ stdcall GetTextCharsetInfo(long ptr long)
@ stdcall GetTextColor(long)
@ stdcall GetTextExtentExPointA(long str long long ptr ptr ptr)
@ stdcall GetTextExtentExPointI(long ptr long long ptr ptr ptr)
@ stdcall GetTextExtentExPointW(long wstr long long ptr ptr ptr)
@ stub GetTextExtentExPointWPri
@ stdcall GetTextExtentPoint32A(long str long ptr)
@ stdcall GetTextExtentPoint32W(long wstr long ptr)
@ stdcall GetTextExtentPointA(long str long ptr)
@ stdcall GetTextExtentPointI(long ptr long ptr)
@ stdcall GetTextExtentPointW(long wstr long ptr)
@ stdcall GetTextFaceA(long long ptr)
@ stub GetTextFaceAliasW
@ stdcall GetTextFaceW(long long ptr)
@ stdcall GetTextMetricsA(long ptr)
@ stdcall GetTextMetricsW(long ptr)
@ stdcall GetTransform(long long ptr)
@ stdcall GetViewportExtEx(long ptr)
@ stdcall GetViewportOrgEx(long ptr)
@ stdcall GetWinMetaFileBits(long long ptr long long)
@ stdcall GetWindowExtEx(long ptr)
@ stdcall GetWindowOrgEx(long ptr)
@ stdcall GetWorldTransform(long ptr)
@ stdcall IntersectClipRect(long long long long long)
@ stdcall InvertRgn(long long)
@ stub IsValidEnhMetaRecord
@ stub IsValidEnhMetaRecordOffExt
@ stdcall LPtoDP(long ptr long)
@ stdcall LineDDA(long long long long ptr long)
@ stdcall LineTo(long long long)
@ stub LoadImageColorMatcherA
@ stub LoadImageColorMatcherW
@ stdcall MaskBlt(long long long long long long long long long long long long)
@ stdcall MirrorRgn(long long)
@ stdcall ModifyWorldTransform(long ptr long)
@ stdcall MoveToEx(long long long ptr)
@ stdcall NamedEscape(long wstr long long ptr long ptr)
@ stdcall OffsetClipRgn(long long long)
@ stdcall OffsetRgn(long long long)
@ stdcall OffsetViewportOrgEx(long long long ptr)
@ stdcall OffsetWindowOrgEx(long long long ptr)
@ stdcall PaintRgn(long long)
@ stdcall PatBlt(long long long long long long)
@ stdcall PathToRegion(long)
@ stdcall Pie(long long long long long long long long long)
@ stdcall PlayEnhMetaFile(long long ptr)
@ stdcall PlayEnhMetaFileRecord(long ptr ptr long)
@ stdcall PlayMetaFile(long long)
@ stdcall PlayMetaFileRecord(long ptr ptr long)
@ stdcall PlgBlt(long ptr long long long long long long long long)
@ stdcall PolyBezier(long ptr long)
@ stdcall PolyBezierTo(long ptr long)
@ stdcall PolyDraw(long ptr ptr long)
@ stub PolyPatBlt
@ stdcall PolyPolygon(long ptr ptr long)
@ stdcall PolyPolyline(long ptr ptr long)
@ stdcall PolyTextOutA(long ptr long)
@ stdcall PolyTextOutW(long ptr long)
@ stdcall Polygon(long ptr long)
@ stdcall Polyline(long ptr long)
@ stdcall PolylineTo(long ptr long)
@ stdcall PtInRegion(long long long)
@ stdcall PtVisible(long long long)
@ stub QueryFontAssocStatus
@ stdcall RealizePalette(long)
@ stdcall RectInRegion(long ptr)
@ stdcall RectVisible(long ptr)
@ stdcall Rectangle(long long long long long)
@ stdcall RemoveFontMemResourceEx(ptr)
@ stdcall RemoveFontResourceA(str)
@ stdcall RemoveFontResourceExA(str long ptr)
@ stdcall RemoveFontResourceExW(wstr long ptr)
@ stub RemoveFontResourceTracking
@ stdcall RemoveFontResourceW(wstr)
@ stdcall ResetDCA(long ptr)
@ stdcall ResetDCW(long ptr)
@ stdcall ResizePalette(long long)
@ stdcall RestoreDC(long long)
@ stdcall RoundRect(long long long long long long long)
@ stdcall SaveDC(long)
@ stdcall ScaleViewportExtEx(long long long long long ptr)
@ stdcall ScaleWindowExtEx(long long long long long ptr)
@ stub SelectBrushLocal
@ stdcall SelectClipPath(long long)
@ stdcall SelectClipRgn(long long)
@ stub SelectFontLocal
@ stdcall SelectObject(long long)
@ stdcall SelectPalette(long long long)
@ stdcall SetAbortProc(long ptr)
@ stdcall SetArcDirection(long long)
@ stub SetBitmapAttributes
@ stdcall SetBitmapBits(long long ptr)
@ stdcall SetBitmapDimensionEx(long long long ptr)
@ stdcall SetBkColor(long long)
@ stdcall SetBkMode(long long)
@ stdcall SetBoundsRect(long ptr long)
@ stub SetBrushAttributes
@ stdcall SetBrushOrgEx(long long long ptr)
@ stdcall SetColorAdjustment(long ptr)
@ stdcall SetColorSpace(long long)
@ stdcall SetDCBrushColor(long long)
@ stdcall SetDCPenColor(long long)
@ stdcall SetDIBColorTable(long long long ptr)
@ stdcall SetDIBits(long long long long ptr ptr long)
@ stdcall SetDIBitsToDevice(long long long long long long long long long ptr ptr long)
@ stdcall SetDeviceGammaRamp(long ptr)
@ stdcall SetEnhMetaFileBits(long ptr)
@ stub SetFontEnumeration
@ stdcall SetGraphicsMode(long long)
@ stdcall SetICMMode(long long)
@ stdcall SetICMProfileA(long str)
@ stdcall SetICMProfileW(long wstr)
@ stdcall SetLayout(long long)
@ stub SetLayoutWidth
@ stdcall SetMagicColors(ptr long long)
@ stdcall SetMapMode(long long)
@ stdcall SetMapperFlags(long long)
@ stdcall SetMetaFileBitsEx(long ptr)
@ stdcall SetMetaRgn(long)
@ stdcall SetMiterLimit(long long ptr)
@ stdcall SetObjectOwner(long long)
@ stdcall SetPaletteEntries(long long long ptr)
@ stdcall SetPixel(long long long long)
@ stdcall SetPixelFormat(long long ptr)
@ stdcall SetPixelV(long long long long)
@ stdcall SetPolyFillMode(long long)
@ stdcall SetROP2(long long)
@ stdcall SetRectRgn(long long long long long)
@ stdcall SetRelAbs(long long)
@ stdcall SetStretchBltMode(long long)
@ stdcall SetSystemPaletteUse(long long)
@ stdcall SetTextAlign(long long)
@ stdcall SetTextCharacterExtra(long long)
@ stdcall SetTextColor(long long)
@ stdcall SetTextJustification(long long long)
@ stdcall SetViewportExtEx(long long long ptr)
@ stdcall SetViewportOrgEx(long long long ptr)
@ stdcall SetVirtualResolution(long long long long long)
@ stdcall SetWinMetaFileBits(long ptr long ptr)
@ stdcall SetWindowExtEx(long long long ptr)
@ stdcall SetWindowOrgEx(long long long ptr)
@ stdcall SetWorldTransform(long ptr)
@ stdcall StartDocA(long ptr)
@ stdcall StartDocW(long ptr)
@ stub StartFormPage
@ stdcall StartPage(long)
@ stdcall StretchBlt(long long long long long long long long long long long)
@ stdcall StretchDIBits(long long long long long long long long long ptr ptr long long)
@ stdcall StrokeAndFillPath(long)
@ stdcall StrokePath(long)
@ stdcall SwapBuffers(long)
@ stdcall TextOutA(long long long str long)
@ stdcall TextOutW(long long long wstr long)
@ stdcall TranslateCharsetInfo(ptr ptr long)
@ stub UnloadNetworkFonts
@ stdcall UnrealizeObject(long)
@ stdcall UpdateColors(long)
@ stdcall UpdateICMRegKey(long str str long) UpdateICMRegKeyA
@ stdcall UpdateICMRegKeyA(long str str long)
@ stdcall UpdateICMRegKeyW(long wstr wstr long)
@ stdcall WidenPath(long)
@ stub bInitSystemAndFontsDirectoriesW
@ stub bMakePathNameW
@ stub cGetTTFFromFOT
@ stub gdiPlaySpoolStream
@ extern pfnRealizePalette
@ extern pfnSelectPalette
@ stub pstackConnect

################################################################
# Wine extensions: OpenGL support
#
@ stdcall wglCopyContext(long long long)
@ stdcall wglCreateContext(long)
@ stdcall wglDeleteContext(long)
@ stdcall wglGetCurrentContext()
@ stdcall wglGetCurrentDC()
@ stdcall -private wglGetProcAddress(str)
@ stdcall wglMakeCurrent(long long)
@ stdcall wglShareLists(long long)
@ stdcall wglUseFontBitmapsA(long long long long)
@ stdcall wglUseFontBitmapsW(long long long long)

################################################################
# Wine extensions: Win16 functions that are needed by other dlls
#
@ stdcall GetDCHook(long ptr)
@ stdcall SetDCHook(long ptr long)
@ stdcall SetHookFlags(long long)

################################################################
# Wine internal extensions
#
# All functions must be prefixed with '__wine_' (for internal functions)
# or 'wine_' (for user-visible functions) to avoid namespace conflicts.

# GDI objects
@ cdecl __wine_make_gdi_object_system(long long)
@ cdecl __wine_set_visible_region(long long ptr)