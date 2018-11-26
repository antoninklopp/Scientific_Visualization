# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1128, 758]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.99999999998727, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2.16261017317024, 46.3371612595104, 64.2005781312117]
renderView1.CameraFocalPoint = [2.16261017317024, 46.3371612595104, 0.0]
renderView1.CameraParallelScale = 11.2818912307014

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
meteonc = NetCDFReader(FileName=[sys.argv[1]])
meteonc.Dimensions = '(latitude, longitude)'
meteonc.SphericalCoordinates = 0
meteonc.ReplaceFillValueWithNan = 1

# create a new 'Calculator'
calculator1 = Calculator(Input=meteonc)
calculator1.Function = 'iHat*UGRD_10maboveground+jHat*VGRD_10maboveground'

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'RH_2maboveground']
glyph1.Vectors = ['POINTS', 'Result']
glyph1.ScaleFactor = 0.3
glyph1.GlyphTransform = 'Transform2'

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['POINTS', 'Result']
streamTracer2.MaximumStreamlineLength = 27.999999999974534

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer2.SeedType.Point1 = [1.4846879353765703, 37.529767523036156, -1.7763568394002505e-14]
streamTracer2.SeedType.Point2 = [6.623230243586854, 55.578605138216886, 0.0]

# create a new 'Contour'
contour1 = Contour(Input=calculator1)
contour1.ContourBy = ['POINTS', 'TMP_2maboveground']
contour1.Isosurfaces = [285.0]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator1,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Result']
streamTracer1.MaximumStreamlineLength = 27.9999999999745

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-5.14258076567153, 38.2186814918074, 0.0]
streamTracer1.SeedType.Point2 = [5.90851405251298, 55.4898351864761, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [258.464172363281, 1.0, 0.0, 1.0, 271.35830954042706, 0.666666666666667, 0.0, 1.0, 273.58996582031205, 0.0, 0.0, 0.498039215686275, 276.3175806474781, 0.0, 0.396078431372549, 0.886274509803922, 278.4252624511721, 0.43921568627451, 0.803921568627451, 1.0, 278.5492553710941, 0.36078431372549, 1.0, 0.756862745098039, 280.7809448242191, 0.0, 1.0, 0.0, 285.86419677734415, 1.0, 1.0, 0.0, 289.2117004394532, 1.0, 0.666666666666667, 0.0, 294.04699707031216, 1.0, 0.0, 0.0, 299.37823486328125, 0.666666666666667, 0.0, 0.0]
tMP2mabovegroundLUT.NanColor = [1.0, 1.0, 1.0]
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [258.464172363281, 1.0, 0.5, 0.0, 299.37823486328125, 1.0, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from meteonc
meteoncDisplay = Show(meteonc, renderView1)
# trace defaults for the display properties.
meteoncDisplay.Representation = 'Slice'
meteoncDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
meteoncDisplay.LookupTable = tMP2mabovegroundLUT
meteoncDisplay.ScalarOpacityUnitDistance = 0.194190573529865

# show color legend
meteoncDisplay.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP2mabovegroundLUT in view renderView1
tMP2mabovegroundLUTColorBar = GetScalarBar(tMP2mabovegroundLUT, renderView1)
tMP2mabovegroundLUTColorBar.Position = [0.893691215616681, 0.561367239101718]
tMP2mabovegroundLUTColorBar.Position2 = [0.120000000000001, 0.43]
tMP2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP2mabovegroundLUTColorBar.ComponentTitle = ''
tMP2mabovegroundLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
tMP2mabovegroundLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

output = "images/" + sys.argv[2] + ".png"
print("fichier sortie", output)
WriteImage(output)
