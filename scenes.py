from objects import *
from materials import *


GLOBALWORLD = Scene()


def setup_testscene():

    # pos x = towards you, neg x is away from you
    # pos z = left, neg z = right
    # pos y = up, neg y = down
    global GLOBALWORLD

    ground_material = Lambertian(Color(0.5, 0.5, 0.5))
    GLOBALWORLD.add(Sphere(Point3(0.0, -1000.0, 0.0), 1000.0, ground_material))

    albedo = Color(0.75, 0.55, 0.89)
    sphere_material = Lambertian(albedo)
    center = Point3(3.0, 0.2, 2.7)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    albedo = Color(0.59, 0.82, 0.91)
    sphere_material = Metal(albedo, 0.15)
    center = Point3(-0.5, 0.2, 1.2)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    sphere_material = Dielectric(1.5)
    center = Point3(1, 0.2, 1.95)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    big_glass_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(Point3(0.0, 1.0, 0.0), 1.0, big_glass_material))

    big_diffuse_material = Lambertian(Color(0.4, 0.2, 0.1))
    GLOBALWORLD.add(Sphere(Point3(-4.0, 1.0, 0.0), 1.0, big_diffuse_material))

    big_metal_material = Metal(Color(0.7, 0.6, 0.5), 0.0)
    GLOBALWORLD.add(Sphere(Point3(4.0, 1.0, 0.0), 1.0, big_metal_material))


def generate_fancymarbles():
    global GLOBALWORLD
    ground_material = Lambertian(Color(0.5, 0.5, 0.5))
    GLOBALWORLD.add(Sphere(Point3(0.0, -1000.0, 0.0), 1000.0, ground_material))

    center = Point3(-8.555529948009356, 0.2, -8.997982124764661)
    albedo = Color(0.8344653411197253, 0.8379595352753051, 0.31571125931805505)
    fuzz = 0.19164057447067812
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.336094444193204, 0.2, -7.440880133589106)
    albedo = Color(0.4720414720285989, 0.44108973343913843, 0.581315060001253)
    fuzz = 0.4483375257166804
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.613543566622548, 0.2, -6.436607950441541)
    albedo = Color(0.5204737504241242, 0.5961406887288925, 0.8265239692043433)
    fuzz = 0.1559840868766585
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.595163074054826, 0.2, -5.607402563416354)
    albedo = Color(0.07023093222097089, 0.26116406087353805, 0.4421797859765337)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.903421158307559, 0.2, -4.130906089614654)
    albedo = Color(0.00517156197357502, 0.1366897867359937, 0.1069670687430551)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.831513927969354, 0.2, -3.8931142949264927)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.533836751528563, 0.2, -2.4345647026655577)
    albedo = Color(0.6225381246439872, 0.17323997410699948, 0.10107609771876447)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.192866079113328, 0.2, -1.7571719202693261)
    albedo = Color(0.07210938439029162, 0.01073181952929436, 0.06757143910424221)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.376778597487373, 0.2, -0.19682102798990053)
    albedo = Color(0.8300333400340827, 0.48984853226807706, 0.43215575650224436)
    fuzz = 0.1809356190981295
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.737641380244547, 0.2, 0.036581388122896165)
    albedo = Color(0.03229278508595102, 0.06079999161221805, 0.4824064697259728)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.925730924578573, 0.2, 1.2625011143845395)
    albedo = Color(0.45329960611654546, 0.030077036790551792, 0.1846574695613805)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.35529905843101, 0.2, 2.8749013767702047)
    albedo = Color(0.4114514384696675, 0.3758358095551748, 0.4346880040148785)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.197949478464954, 0.2, 3.571530546858426)
    albedo = Color(0.18392619446149094, 0.4340828682671751, 0.3914726272361291)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.647112587143559, 0.2, 4.534122356383479)
    albedo = Color(0.015029144330178072, 0.712081473212949, 0.4511036727574616)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.170242816005045, 0.2, 5.793155020556376)
    albedo = Color(0.11624905604530099, 0.0070818222727631755, 0.05670443519779697)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.915207289595223, 0.2, 6.239196473380253)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.902310841796593, 0.2, 7.2742380620638745)
    albedo = Color(0.6260783599983054, 0.19984112662657835, 0.5200557258025423)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-8.533169733568966, 0.2, 8.019625403298777)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.5980145001020025, 0.2, -8.138814230837678)
    albedo = Color(0.5900267779480663, 0.8265403093411001, 0.47844768663781345)
    fuzz = 0.35311655458143554
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.922440743732559, 0.2, -7.63663149685136)
    albedo = Color(0.268915175287745, 0.3056623446570151, 0.04340360718750775)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.9061971313827115, 0.2, -6.357835913732449)
    albedo = Color(0.03085728090617867, 0.5185426380148949, 0.6268095002620386)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.881810806181758, 0.2, -5.603321013743473)
    albedo = Color(0.22169426688285276, 0.19289967441756864, 0.2183045583281597)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.286896906013132, 0.2, -4.515741177728559)
    albedo = Color(0.5004662368781445, 0.4738236040914923, 0.7115372257101812)
    fuzz = 0.1356624955333664
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.5999698263332265, 0.2, -3.5172198826673213)
    albedo = Color(0.2791801879640588, 0.4016340908618638, 0.495541141533259)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.680510477685983, 0.2, -2.756396672999052)
    albedo = Color(0.06812131868384709, 0.8432063017091013, 0.0209065171428089)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.4793886101366525, 0.2, -1.1743841977259133)
    albedo = Color(0.020925044134759953, 0.25813587430920554, 0.7732818827435841)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.385175174570983, 0.2, -0.8366166198821502)
    albedo = Color(0.43169722446561004, 0.03882825326080134, 0.10066054267959898)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.402284112850179, 0.2, 0.3696892051622491)
    albedo = Color(0.30997531332801764, 0.04330618892114067, 0.4484408098356913)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.304149815088923, 0.2, 1.8388778013876381)
    albedo = Color(0.05038165063616508, 0.09158167465375848, 0.42327590142056787)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.6987079043148805, 0.2, 2.612869864417302)
    albedo = Color(0.38342125690999435, 0.5499237600964699, 0.29306783389430885)
    fuzz = 0.18928821477093932
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.9819813430380675, 0.2, 3.158666858331238)
    albedo = Color(0.31537596674315593, 0.03655356712294174, 0.07487693644046532)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.554418320525679, 0.2, 4.261710892503652)
    albedo = Color(0.21612111783583784, 0.11838501266385913, 0.22803274863518652)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.956815728974219, 0.2, 5.498084867000219)
    albedo = Color(0.011031669068456696, 0.7130007961984243, 0.043798431439885724)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.371337895113244, 0.2, 6.384658704165863)
    albedo = Color(0.1319752655562647, 0.07088403418199349, 0.18337513901117888)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.235750962706895, 0.2, 7.134093438137176)
    albedo = Color(0.16043047651705858, 0.8636428063405612, 0.47106763773230803)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-7.661505549451369, 0.2, 8.712902367113506)
    albedo = Color(0.7088091647387659, 0.56756604114462, 0.5355499949208938)
    fuzz = 0.4563825679241243
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.979954441592833, 0.2, -8.889992239760353)
    albedo = Color(0.37611307164206215, 0.15108223689125644, 0.33118255533784124)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.611799368960055, 0.2, -7.489138941659263)
    albedo = Color(0.44385304465464037, 0.3454599097311569, 0.6453625133517574)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.1349736502624, 0.2, -6.218841797646298)
    albedo = Color(0.14075682968828543, 0.08065463240222798, 0.06917454926561169)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.519785322862254, 0.2, -5.151434229448257)
    albedo = Color(0.11716452149744201, 0.020979592525483922, 0.27746741748289766)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.459121398111008, 0.2, -4.407306952951545)
    albedo = Color(0.16734546852873472, 0.24648109647667493, 0.2282753930166908)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.56348434299052, 0.2, -3.105925608269246)
    albedo = Color(0.14859957593997572, 0.5322540225503177, 0.47430164209457143)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.65425736829277, 0.2, -2.9883819007197383)
    albedo = Color(0.12612264745817914, 0.3365963066882019, 0.30699875983162844)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.519642261262567, 0.2, -1.6779356411844024)
    albedo = Color(0.6319246735434668, 0.10319363461196975, 0.06458218114777146)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.138961978209042, 0.2, -0.27624982431073475)
    albedo = Color(0.005786612296525246, 0.4451016960041981, 0.0936072722564364)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.959383751689581, 0.2, 0.3220980767746028)
    albedo = Color(0.13736686171386375, 0.5699735930425144, 0.0470944124117204)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.677504890461123, 0.2, 1.7178948391392028)
    albedo = Color(0.4912446931701407, 0.01261226267441325, 0.026036016766986216)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.438048515482252, 0.2, 2.4554965880836366)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.274355557930109, 0.2, 3.0871011631703293)
    albedo = Color(0.6980388849484642, 0.31752316911802336, 0.06565350071013379)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.916758239120892, 0.2, 4.713338095704465)
    albedo = Color(0.00045549632144882676, 0.18313196856302894, 0.150603751159368)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.36148049874277, 0.2, 5.178202223334799)
    albedo = Color(0.015712702872504945, 0.060345762777342, 0.23948225612199195)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.321175441691738, 0.2, 6.55829038883772)
    albedo = Color(0.5232704067232458, 0.4136724128516856, 0.2098439663762407)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.58763142266136, 0.2, 7.746089092392391)
    albedo = Color(0.5637922251109786, 0.5067776276382786, 0.6672921301796093)
    fuzz = 0.16304899660189753
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-6.754409526300305, 0.2, 8.0029696527472)
    albedo = Color(0.21507316856770944, 0.0950960936955649, 0.24623555376261522)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.618511237148498, 0.2, -8.615664310995857)
    albedo = Color(0.17377069954639188, 0.29646719028398577, 0.7114065825340485)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.6862518888383615, 0.2, -7.744398435717593)
    albedo = Color(0.8284703987712578, 0.32626286697028534, 0.33065219296951814)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.423762032532297, 0.2, -6.103615957834946)
    albedo = Color(0.07426774724618462, 0.21382975358120834, 0.2525882159304507)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.213654076064443, 0.2, -5.7084631041674365)
    albedo = Color(0.2407210842975494, 0.3306080142653905, 0.5707863889133689)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.945313057868074, 0.2, -4.597402841491722)
    albedo = Color(0.07867926750164443, 0.0846565373935172, 0.17065929185718465)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.903436774620855, 0.2, -3.6471084246277004)
    albedo = Color(0.5869952986994573, 0.22895415403193717, 0.38466347836251524)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.706359914583781, 0.2, -2.4112004086132903)
    albedo = Color(0.20609063339125674, 0.6140994539690338, 0.5258719228381461)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.696748056408947, 0.2, -1.470262239521826)
    albedo = Color(0.6497459180135409, 0.3329665547300913, 0.5275119570927104)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.2540826806394945, 0.2, -0.6005774030656501)
    albedo = Color(0.4097587301965232, 0.39746119385054607, 0.7407963538888344)
    fuzz = 0.37528685319452426
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.8411018648571895, 0.2, 0.12988712392719662)
    albedo = Color(0.787964624117971, 0.4561766346812018, 0.016185972301874924)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.60298417574637, 0.2, 1.40298410978472)
    albedo = Color(0.6861446986306464, 0.13749119119082626, 0.07239252158855902)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.508454686985316, 0.2, 2.8877996136903263)
    albedo = Color(0.3338086303077687, 0.12086375297433434, 0.13479084737984484)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.108515726475683, 0.2, 3.13686201176894)
    albedo = Color(0.5063977236646962, 0.20159020226803306, 0.1448430419893845)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.231386832276918, 0.2, 4.48270366355496)
    albedo = Color(0.05784313347430407, 0.42156513322904654, 0.10857611155946822)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.328163659011232, 0.2, 5.635493512895015)
    albedo = Color(0.089738955514629, 0.24989440684481148, 0.13557460436463048)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.699539200834984, 0.2, 6.578130106092902)
    albedo = Color(0.1255602626534933, 0.04586481189419549, 0.19453594585888823)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.584072987979013, 0.2, 7.15086455156949)
    albedo = Color(0.040290902738545624, 0.47070017487884847, 0.24326413421615425)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-5.485767150443507, 0.2, 8.599178538045209)
    albedo = Color(0.5283759680460614, 0.5436189312137543, 0.2519558818332395)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.767136267770563, 0.2, -8.916414463925033)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.143819375101648, 0.2, -7.624874038226686)
    albedo = Color(0.4132911813697071, 0.2320131836974814, 0.12385961512486007)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.6906408855453074, 0.2, -6.620872619020354)
    albedo = Color(0.13575659671441986, 0.12540531817447637, 0.5117610915063068)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.811749849773077, 0.2, -5.6623043565003846)
    albedo = Color(0.4962820933767056, 0.19432577225142889, 0.09450681327756118)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.348314415725797, 0.2, -4.648667533954572)
    albedo = Color(0.40510291778866453, 0.7921440781122259, 0.6576813890943836)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.542071752072658, 0.2, -3.1497411466565066)
    albedo = Color(0.48052298267465493, 0.04865626653514803, 0.005485610578868969)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.271770883217062, 0.2, -2.223461612154813)
    albedo = Color(0.1318162796024324, 0.5759834352949158, 0.12821740698975248)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.558454675806572, 0.2, -1.330962879132318)
    albedo = Color(0.10556428526081442, 0.6265275546651005, 0.7702302223972283)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.938857117391267, 0.2, -0.5353338900717142)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.630007017795255, 0.2, 0.624320726042944)
    albedo = Color(0.015686148266563504, 0.047742521166859966, 0.0009846869442293026)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.97949991512096, 0.2, 1.4764984301149062)
    albedo = Color(0.8585191793664183, 0.5473344968084172, 0.5303194681824123)
    fuzz = 0.019771171580196645
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.783752312013025, 0.2, 2.4450794981321624)
    albedo = Color(0.3504477446211906, 0.42015739730592006, 0.19470042163749024)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.79725737746297, 0.2, 3.219844469167628)
    albedo = Color(0.13356283841025154, 0.052906192028544144, 0.7117072089906341)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.507538336905579, 0.2, 4.849147043030608)
    albedo = Color(0.6643076565502298, 0.7178760630581497, 0.6796274877902253)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.668824477866557, 0.2, 5.030464771249873)
    albedo = Color(0.08449903909260399, 0.38789448619416916, 0.7768809965854444)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.104090655168205, 0.2, 6.527949727477929)
    albedo = Color(0.8210583201349184, 0.5449881912197692, 0.11485943785573924)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.87068916957959, 0.2, 7.461569204304838)
    albedo = Color(0.19946272980387564, 0.15015673395417697, 0.16883643402686363)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-4.444008653487194, 0.2, 8.652814891703722)
    albedo = Color(0.3666432752112639, 0.1718279425063281, 0.007558854090757814)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.9518982263303193, 0.2, -8.524429428028643)
    albedo = Color(0.020755544141469635, 0.3584793077609972, 0.3248053513361879)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.2473872783695623, 0.2, -7.685962490698297)
    albedo = Color(0.6160469078960106, 0.11377538815287784, 0.16202798635330534)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.4879446292995606, 0.2, -6.263441896558795)
    albedo = Color(0.1359742178837231, 0.07172898406285187, 0.00919181854502809)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.822586354865773, 0.2, -5.120841883576258)
    albedo = Color(0.21222110508808031, 0.14113383878311536, 0.06183018304250789)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.9614025826066057, 0.2, -4.1898717453398255)
    albedo = Color(0.5567996623979519, 0.44179643452655964, 0.03504674015737133)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.8482551256676074, 0.2, -3.4235756017682446)
    albedo = Color(0.17207921207397253, 0.14002567602471028, 0.39536715088072016)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.564119621389505, 0.2, -2.6303011867593273)
    albedo = Color(0.6432635784677145, 0.7671049832871344, 0.48552953109734237)
    fuzz = 0.1326809560278004
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.241144725914511, 0.2, -1.1059667911978686)
    albedo = Color(0.3162322926701045, 0.47945953109875744, 0.7978475770679647)
    fuzz = 0.1328033191593968
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.56296435661179, 0.2, -0.29974894741059077)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.543618399918998, 0.2, 0.1636983686781421)
    albedo = Color(0.30538432421341594, 0.1565381471850202, 0.7020751341633569)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.4307732572067953, 0.2, 1.1935257051560764)
    albedo = Color(0.5208386356531944, 0.0297065088143874, 0.8488898638189897)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.5418676115605607, 0.2, 2.007697266031106)
    albedo = Color(0.0005472799143554434, 0.010819648441192087, 0.1616978384453303)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.817604638236937, 0.2, 3.0147051692047344)
    albedo = Color(0.0825447083247617, 0.44361907751341545, 0.6570974142078363)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.5544274099618884, 0.2, 4.180306700182807)
    albedo = Color(0.013776173082121155, 0.07954847382033683, 0.6936687020418073)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.3248977275360385, 0.2, 5.036327679260643)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.5933750158987996, 0.2, 6.108111258876489)
    albedo = Color(0.19912355213596902, 0.45178893763208616, 0.059000791970457066)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.767441047552321, 0.2, 7.251175975217009)
    albedo = Color(0.7606177707407241, 0.5021329630570888, 0.2640935627406751)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-3.788356543398471, 0.2, 8.68575071002283)
    albedo = Color(0.15051869758535366, 0.02092952512639474, 0.0008617180429050911)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.5197551418275745, 0.2, -8.44289528071047)
    albedo = Color(0.7397337467971326, 0.48965538187235297, 0.7308311273581528)
    fuzz = 0.2434849630212219
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.615576570648007, 0.2, -7.883507389477392)
    albedo = Color(0.3154088234429474, 0.017899466477118722, 0.545423951751996)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.76699129327009, 0.2, -6.858361846188095)
    albedo = Color(0.2872889491996177, 0.20294471529064392, 0.18449446994822172)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.458864295712651, 0.2, -5.5767913909967834)
    albedo = Color(0.42878114515330396, 0.7682523195773653, 0.7367521284407482)
    fuzz = 0.4584404880397049
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.1266729836781755, 0.2, -4.344352142031343)
    albedo = Color(0.8077949760104226, 0.09253489958437594, 0.23936225888022003)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.7397444501130126, 0.2, -3.3083562008755)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.7200414618445095, 0.2, -2.1529591490785553)
    albedo = Color(0.008052564256417125, 0.14579434892887597, 0.1947173020641088)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.5250475782445143, 0.2, -1.1848533520442128)
    albedo = Color(0.34371384306949804, 0.2583400939832417, 0.2464361306225489)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.3039812467546845, 0.2, -0.7313525136394035)
    albedo = Color(0.07153599386413717, 0.31807602387872574, 0.8620390703832638)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.3328633332166118, 0.2, 0.27781993203442673)
    albedo = Color(0.469253912114902, 0.03449183722967936, 0.48094825776926386)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.1212478482666284, 0.2, 1.3817120815112691)
    albedo = Color(0.02057270265885601, 0.09940456162757778, 0.5199551219327364)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.5943280109346385, 0.2, 2.6633526961241647)
    albedo = Color(0.16048847085818915, 0.007790811103903407, 0.01436744271784059)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.139927654152457, 0.2, 3.7774258646885346)
    albedo = Color(0.09255977716556829, 0.13447062681174332, 0.14859896270298192)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.914812678329276, 0.2, 4.4265874018946345)
    albedo = Color(0.6560339703741014, 0.6879145043982628, 0.6258691287995899)
    fuzz = 0.2916082660881367
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.1093412635386066, 0.2, 5.725410573085074)
    albedo = Color(0.6137371680514361, 0.7520508469094004, 0.3945352438076976)
    fuzz = 0.230003280508008
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.8834739885657177, 0.2, 6.67192472999202)
    albedo = Color(0.3291526656883375, 0.20164355590887353, 0.6884377022540111)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.8122170091012006, 0.2, 7.72852503971658)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-2.9348126866279114, 0.2, 8.468782970729032)
    albedo = Color(0.5653552825390932, 0.03269458335657131, 0.06267361354461916)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.1134433311681367, 0.2, -8.780265400850809)
    albedo = Color(0.30326624110707195, 0.3559011418756269, 0.33940557225383977)
    fuzz = 0.2289538904840463
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.1709231366346837, 0.2, -7.234982699193424)
    albedo = Color(0.4797855788270836, 0.36692907135145153, 0.15768841840732217)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.1620922380923822, 0.2, -6.8703379099865165)
    albedo = Color(0.5480471818500867, 0.004169503722698037, 0.8971823879780082)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.9800129680998058, 0.2, -5.636310298426714)
    albedo = Color(0.5139485413129099, 0.4736708878361076, 0.8096220676953487)
    fuzz = 0.2890812875706388
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.5389987144842483, 0.2, -4.727843587212066)
    albedo = Color(0.02874843591017573, 0.3659150464757186, 0.41147287555007045)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.445342622292735, 0.2, -3.3859130113035407)
    albedo = Color(0.3297455638191011, 0.013355287372330911, 0.24683283258150665)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.9926839646167396, 0.2, -2.1978234838791875)
    albedo = Color(0.633820604899765, 0.4862019764831562, 0.28056025746088903)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.5935826969602216, 0.2, -1.1654059726108907)
    albedo = Color(0.3848155301412605, 0.6404496291957877, 0.29215836684691987)
    fuzz = 0.40180025396798286
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.1855177780249666, 0.2, -0.5875187736199091)
    albedo = Color(0.4172256938157997, 0.48772296655643554, 0.05599123364587126)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.738063784299549, 0.2, 0.6022120063352058)
    albedo = Color(0.12637739082986513, 0.4426956756892925, 0.4806969277876292)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.5583759236697257, 0.2, 1.3299142586983057)
    albedo = Color(0.635908626580599, 0.5474927365279961, 0.40277528472818847)
    fuzz = 0.4409764700696176
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.5847951651508339, 0.2, 2.07202408928478)
    albedo = Color(0.8818820036771844, 0.6056632281306474, 0.6018946553923769)
    fuzz = 0.02599499484327239
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.2773049155247322, 0.2, 3.7573891436645024)
    albedo = Color(0.7241226062640153, 0.009955645124681138, 0.07850668150908875)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.2599353560823974, 0.2, 4.578998991533377)
    albedo = Color(0.09452424054841482, 0.32646818324475774, 0.05333206153994702)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.7399173891237691, 0.2, 5.775028266728134)
    albedo = Color(0.022743035908054446, 0.07629688557569535, 0.21103456842899906)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.8963851522073754, 0.2, 6.577427355516717)
    albedo = Color(0.41940092760582426, 0.8480740572236672, 0.895688117546903)
    fuzz = 0.4042344595503125
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.2346696919487572, 0.2, 7.345889483983314)
    albedo = Color(0.5218303710452926, 0.3847422261948535, 0.749267806747538)
    fuzz = 0.38421278184141294
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-1.8263305721747172, 0.2, 8.585954019058534)
    albedo = Color(0.6748764144974768, 0.0007540521861405989, 0.6542056780999125)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.10575239100350864, 0.2, -8.229991455822288)
    albedo = Color(0.0302485254374818, 0.49890065348815194, 0.060424964074944014)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.9001222126154874, 0.2, -7.995714574866592)
    albedo = Color(0.7446434577597879, 0.10477198481415487, 0.04160481568235926)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.478829561560034, 0.2, -6.282502710210499)
    albedo = Color(0.07832484551538095, 0.4280186675662806, 0.07914287980328842)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.88186968523532, 0.2, -5.331555864387237)
    albedo = Color(0.713158110612661, 0.04990323400109147, 0.17248161157314507)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.18511680638102856, 0.2, -4.717643534311837)
    albedo = Color(0.6233374349677219, 0.3431517822418538, 0.06100353420384684)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.9268552932405263, 0.2, -3.353541061607262)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.13288722808645714, 0.2, -2.940790346974791)
    albedo = Color(0.39298346996518485, 0.27146752328873847, 0.026973839816212694)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.8882621550437906, 0.2, -1.1120946800242528)
    albedo = Color(0.3670414798060458, 0.26811833090242754, 0.008012283212750864)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.5741741974552124, 0.2, -0.7832689198554051)
    albedo = Color(0.3558365116764564, 0.3099372957043935, 0.23675734531277784)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.662710245621096, 0.2, 0.4678802815670996)
    albedo = Color(0.4837960474667929, 0.4144916775120431, 0.46378751933114637)
    fuzz = 0.1092345869479816
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.5495860836801841, 0.2, 1.4130153582507652)
    albedo = Color(0.35689548814163297, 0.0025988204700502083, 0.27005871004109044)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.605933629437392, 0.2, 2.307127249824548)
    albedo = Color(0.34732220795012775, 0.02454351106007548, 0.757335442908077)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.12409706969890733, 0.2, 3.6968270660845213)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.3464237794582977, 0.2, 4.42389568504883)
    albedo = Color(0.1360931941069712, 0.15681013135815886, 0.12324190207231873)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.2853039902595489, 0.2, 5.09408855821752)
    albedo = Color(0.04650103493492741, 0.38937968486902313, 0.035942374400138824)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.8879040397449636, 0.2, 6.150499423684191)
    albedo = Color(0.026287888189528638, 0.16165072671869765, 0.06453866093058876)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.2862742160406714, 0.2, 7.617519595863246)
    albedo = Color(0.42714677006552737, 0.5903885332724125, 0.28051982146776994)
    fuzz = 0.053096313092647895
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(-0.4862792294437247, 0.2, 8.438169382935094)
    albedo = Color(0.10303343573106306, 0.09938228688410446, 0.4958595464650136)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.5063363059835018, 0.2, -8.811461053296695)
    albedo = Color(0.0009211793669398567, 0.21190113744176386, 0.011367487215093317)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.31138844409518335, 0.2, -7.777403604161989)
    albedo = Color(0.6947434358264254, 0.6255896096910154, 0.6793463621799376)
    fuzz = 0.433244647339378
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.6231456223137135, 0.2, -6.335612876666204)
    albedo = Color(0.21702674010479914, 0.16517269790524142, 0.6561764492886213)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.1634830011429726, 0.2, -5.984279437052305)
    albedo = Color(0.26123255311068555, 0.029177040326868516, 0.6231871101356167)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.26426226955200627, 0.2, -4.7473028172878)
    albedo = Color(0.8599815466262377, 0.04641414932852453, 0.6099129000092522)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.6548355231634032, 0.2, -3.870283419178101)
    albedo = Color(0.7813782565605645, 0.9413071519306679, 0.8102617328416971)
    fuzz = 0.07135961418035897
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.7416808758547181, 0.2, -2.1671966079888616)
    albedo = Color(0.15929545981340248, 0.42362833021559454, 0.01619991944958162)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.10136376180372049, 0.2, -1.516745434902087)
    albedo = Color(0.9126836539588884, 0.439987424051323, 0.5178489320699056)
    fuzz = 0.32087620917372567
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.44015660844975685, 0.2, -0.6697304469953634)
    albedo = Color(0.38347431237534485, 0.5492854636051602, 0.03325990524958926)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.3138086688975482, 0.2, 0.08544383122833027)
    albedo = Color(0.5176484894395843, 0.3091117799731115, 0.016602360566947427)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.046617955454879755, 0.2, 1.220869381583492)
    albedo = Color(0.5131626148555336, 0.06981183546165137, 0.006736014123380182)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.42522961758963, 0.2, 2.3329928435037672)
    albedo = Color(0.5886655180527834, 0.39185495447715113, 0.8354673903530416)
    fuzz = 0.03762971299604673
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.8750042890314508, 0.2, 3.8257179321711905)
    albedo = Color(0.22811071615794046, 0.39903591422714674, 0.41130683849947985)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.3030708030610998, 0.2, 4.05201142307061)
    albedo = Color(0.3274751402483503, 0.3184574681757551, 0.05648922656865481)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.04355586387293895, 0.2, 5.129332969386828)
    albedo = Color(0.19885978219056416, 0.16990572281732066, 0.26156385488303124)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.8952146465053269, 0.2, 6.340768827108322)
    albedo = Color(0.07314517094300507, 0.0704706305120562, 0.45881587641154414)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.3530305331790995, 0.2, 7.195784371789344)
    albedo = Color(0.0413689798129947, 0.17845027521073717, 0.7509269643496294)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(0.45158181365114314, 0.2, 8.458157622871981)
    albedo = Color(0.1383690872203762, 0.3624213841209395, 0.02865275611223595)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.6685246114614505, 0.2, -8.80443092012814)
    albedo = Color(0.0388037590612234, 0.2777888382673442, 0.12748717309009863)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.0659653429656, 0.2, -7.628063772049023)
    albedo = Color(0.1320356647103754, 0.006688736054004609, 0.008475344638211174)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.7955086003422847, 0.2, -6.503899571158998)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.2063705395467583, 0.2, -5.696421511919186)
    albedo = Color(0.6250598186654425, 0.48115242543645054, 0.5455425758630895)
    fuzz = 0.06854813494010586
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.7867789107038947, 0.2, -4.351567561155052)
    albedo = Color(0.2266482851805957, 0.11964497350353076, 0.4120932708694802)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.7451077997047018, 0.2, -3.9916473313274143)
    albedo = Color(0.5444025363754482, 0.4695157608640075, 0.7721057445058109)
    fuzz = 0.24378462327522182
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.51350315881799, 0.2, -2.9632866742792934)
    albedo = Color(0.4315880225694305, 0.36354751481115116, 0.7464737272013376)
    fuzz = 0.16529456269787196
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.2292544043325424, 0.2, -1.7198943499571253)
    albedo = Color(0.11034793614332837, 0.04014044535076995, 0.0501527361468333)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.501896157865249, 0.2, -0.9123439269138853)
    albedo = Color(0.6074712966098219, 0.34291355599784934, 0.4617629796592923)
    fuzz = 0.32962692522004505
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.7267581773469294, 0.2, 0.5462478717896305)
    albedo = Color(0.3045272376236888, 0.35845752550663534, 0.032460002762124796)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.8622351213345594, 0.2, 1.8536433245772002)
    albedo = Color(0.3433583024756707, 0.5996082787929894, 0.0007863454175297725)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.552790521979056, 0.2, 2.0285191940181937)
    albedo = Color(0.5634568852049489, 0.43959325697704144, 0.255892495060766)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.1949075276727479, 0.2, 3.379818801464123)
    albedo = Color(0.08134423220634902, 0.055445033019825354, 0.2307804346109249)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.3842399305846183, 0.2, 4.8336733328491)
    albedo = Color(0.28838150591294404, 0.2296006518825966, 0.04726460781209787)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.481840169661298, 0.2, 5.181881028279269)
    albedo = Color(0.5083455509555843, 0.4760996889788382, 0.5258533158010154)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.7625719385618601, 0.2, 6.048233959206269)
    albedo = Color(0.07569145399765875, 0.3027748952102129, 0.3410124707591894)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.3610551536807447, 0.2, 7.323403318191253)
    albedo = Color(0.34793175560387346, 0.5809417729351586, 0.04316010649646577)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(1.187264258353465, 0.2, 8.751545583332229)
    albedo = Color(0.6660314155189442, 0.09992486420980895, 0.012532311570671285)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.3086822399207385, 0.2, -8.10885271547351)
    albedo = Color(0.2225116747921373, 0.08574863296368956, 0.3402492201711904)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.0995244057464477, 0.2, -7.877592458936414)
    albedo = Color(0.7483760083977739, 0.39444913995764885, 0.3941238027452945)
    fuzz = 0.4912175392344222
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.2113269008024043, 0.2, -6.416535738882421)
    albedo = Color(0.2714152297496271, 0.06901669116866094, 0.3699096723532301)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.2728564133419176, 0.2, -5.878535197987678)
    albedo = Color(0.916885054217415, 0.019207070912708044, 0.022608768141083677)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.546281856764986, 0.2, -4.981441502672081)
    albedo = Color(0.16809820070821885, 0.0352426766560757, 0.7102371389860551)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.7671888189409772, 0.2, -3.721491708269661)
    albedo = Color(0.10776293613876754, 0.38211361774190306, 0.10834911670757456)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.6422295993305696, 0.2, -2.444545342331254)
    albedo = Color(0.6188363881441383, 0.4228101866779421, 0.4822594741959695)
    fuzz = 0.08441231810078864
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.3774048817695976, 0.2, -1.7982389333607756)
    albedo = Color(0.14001125345472362, 0.012077734536223227, 0.21416690044493777)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.5723659445447895, 0.2, -0.8416475715963335)
    albedo = Color(0.053066517861323055, 0.3597328691852659, 0.534797082207283)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.015889649177649, 0.2, 0.5840153225300838)
    albedo = Color(0.23532499245359953, 0.12237382170575811, 0.03585640000153346)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.1465324659727933, 0.2, 1.167748963018609)
    albedo = Color(0.20961076853027918, 0.7592176179267427, 0.36936190061597896)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.2302149592332845, 0.2, 2.5304245242113543)
    albedo = Color(0.759169644621236, 0.46285206239940296, 0.5485538952912233)
    fuzz = 0.16124118564088735
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.6718197000509116, 0.2, 3.8125418725780613)
    albedo = Color(0.05916714782165563, 0.2689657146306315, 0.6828571467383449)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.6651237141148054, 0.2, 4.146888508105579)
    albedo = Color(0.035175704017589224, 0.0637685399632625, 0.02129959561615757)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.090308458857401, 0.2, 5.561470574244257)
    albedo = Color(0.11049152896478681, 0.0012603207792312046, 0.14803841615899052)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.8412429169796276, 0.2, 6.848045731224993)
    albedo = Color(0.05872464825453094, 0.3378895530799255, 0.34485278250307877)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.180991549898898, 0.2, 7.873868248900894)
    albedo = Color(0.1857628587024102, 0.5683375361696393, 0.17415392493272175)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(2.1444018673714527, 0.2, 8.581987987341355)
    albedo = Color(0.06030538488330232, 0.188010222316785, 0.2179991948776183)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.392500655024268, 0.2, -8.881541317397112)
    albedo = Color(0.4521300108475714, 0.3691891448427424, 0.4534082237082768)
    fuzz = 0.027287352205781934
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.6458923628482847, 0.2, -7.575735020756601)
    albedo = Color(0.03515154131420223, 0.19357714917385496, 0.3171145860759656)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.7307592194534456, 0.2, -6.994659553203561)
    albedo = Color(0.49062626643490903, 0.13121919405160545, 0.005701929574168195)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.5510572773602855, 0.2, -5.253310035087524)
    albedo = Color(0.30893310200174645, 0.6588679947930051, 0.3312436370939912)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.2847344580271622, 0.2, -4.793928647019149)
    albedo = Color(0.7178203335053325, 0.16703371032060377, 0.739636126113627)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.741662676253955, 0.2, -3.702018055251505)
    albedo = Color(0.3776362398457878, 0.37184699617896333, 0.6302521794896486)
    fuzz = 0.27930826767982736
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.0281395596935115, 0.2, -2.2974153484738937)
    albedo = Color(0.23231286358371858, 0.3420014121526827, 0.5572922455384781)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.334496502976478, 0.2, -1.46152154792951)
    albedo = Color(0.42580960850021116, 0.1564471157575509, 0.31983194428323847)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.540675565518013, 0.2, 1.4398225598397112)
    albedo = Color(0.1309197817776485, 0.1837367240119999, 0.3449665804184634)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.0775379773890807, 0.2, 2.2308730025011285)
    albedo = Color(0.4828092625142775, 0.7099890980422299, 0.4170621027051495)
    fuzz = 0.0338324286385987
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.5942330982053448, 0.2, 3.3214048872977013)
    albedo = Color(0.3250599623172177, 0.4674363210106453, 0.513787776315624)
    fuzz = 0.40632222304129356
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.848411803218867, 0.2, 4.776987934198416)
    albedo = Color(0.1248579056209444, 0.004805242441511963, 0.050737539618938975)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.856723936864735, 0.2, 5.431037753713385)
    albedo = Color(0.4626826622038406, 0.4677723442735892, 0.48705694662594073)
    fuzz = 0.2436751634171503
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.3413220668962693, 0.2, 6.471007718950969)
    albedo = Color(0.6392189728883019, 0.6195321318780588, 0.5640608810944165)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.087705895117016, 0.2, 7.214833981521678)
    albedo = Color(0.12368899752163184, 0.23821649449083238, 0.07540858311522777)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(3.5870205086684877, 0.2, 8.780205835606235)
    albedo = Color(0.04321844708376598, 0.8042748372383589, 0.043857860983986814)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.76206618398564, 0.2, -8.861951749910649)
    albedo = Color(0.7026273278296672, 0.6027513007822066, 0.4283470891309305)
    fuzz = 0.48096874087934915
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.4747459279562225, 0.2, -7.1971604384263905)
    albedo = Color(0.0794386025353426, 0.006720663902461948, 0.3270939478952054)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.424822233256321, 0.2, -6.7685485749653465)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.35796701521499, 0.2, -5.4161742289838)
    albedo = Color(0.9026352410690468, 0.817789465614146, 0.4483013345039743)
    fuzz = 0.21366723294292234
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.785222797520447, 0.2, -4.407379960700806)
    albedo = Color(0.08886909320014204, 0.10630970674078788, 0.01044633207832883)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.635048253816344, 0.2, -3.8736199920709558)
    albedo = Color(0.47742610345351866, 0.2587450108853793, 0.05856137976443398)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.343355698649546, 0.2, -2.7434964847256023)
    albedo = Color(0.10226065898798298, 0.4107050884209636, 0.1788072931762618)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.890994082714803, 0.2, -1.4206416079979551)
    albedo = Color(0.19774598644817817, 0.21353651641446783, 0.1683863671557003)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.014712899379226, 0.2, 1.5356942083790415)
    albedo = Color(0.35965599487818795, 0.12869097689238743, 0.3001143198939601)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.132800433449718, 0.2, 2.6361125457243504)
    albedo = Color(0.025829499986475126, 0.2927227530863645, 0.23766556183068802)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.132336470283859, 0.2, 3.5144257471717912)
    albedo = Color(0.023642283756003517, 0.7648699248825541, 0.3186749267028792)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.19176782310161, 0.2, 4.073876193905672)
    albedo = Color(0.4787630170260851, 0.34478607789388477, 0.4892114360503348)
    fuzz = 0.4490178824102732
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.411654588457406, 0.2, 5.364130482736709)
    albedo = Color(0.14060347808442394, 0.7385000555896327, 0.41305471876308625)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.664318360186643, 0.2, 6.022169580995129)
    albedo = Color(0.07296010330155846, 0.6712858478258473, 0.06446301213697302)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.61347306147622, 0.2, 7.877833759476072)
    albedo = Color(0.08658541155046875, 0.22958908563696048, 0.3239716193775907)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(4.512080890764919, 0.2, 8.837855162616387)
    albedo = Color(0.024503939240098003, 0.1342893747495937, 0.06169250422559375)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.51008189255509, 0.2, -8.287009236093105)
    albedo = Color(0.0017565280585976279, 0.09208641697703238, 0.2843830168085834)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.281089827783301, 0.2, -7.548033604777168)
    albedo = Color(0.07718808405676836, 0.02309412124345121, 0.10760353759878785)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.118793034371361, 0.2, -6.378369906767482)
    albedo = Color(0.8263077561347792, 0.6701876915046605, 0.18719362575658932)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.596126158442428, 0.2, -5.752071289612156)
    albedo = Color(0.16357993582807162, 0.08589894528220343, 0.4163811276489885)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.71105009767508, 0.2, -4.241545895502099)
    albedo = Color(0.18156993773033225, 0.4244413535986826, 0.08670748731549272)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.823493135568438, 0.2, -3.4171878760457206)
    albedo = Color(0.5889763567140638, 0.04716590748931179, 0.5771209951784608)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.344460728791018, 0.2, -2.20747943826318)
    albedo = Color(0.2579948690926785, 0.19590738730703175, 0.34482143302853757)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.016193697517448, 0.2, -1.2539078252834157)
    albedo = Color(0.10955193364747867, 0.7032774815655249, 0.03770232228806526)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.555001266169396, 0.2, -0.5454906988173682)
    albedo = Color(0.10377768620720007, 0.015752979078199367, 0.41226750129598516)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.510012375002221, 0.2, 0.15926420254151846)
    albedo = Color(0.12219568517122259, 0.46991347860737076, 0.051920865404266665)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.18195250712509, 0.2, 1.1681323296418538)
    albedo = Color(0.7740874113253986, 0.28409360132114997, 0.45134505187572044)
    fuzz = 0.22418525779755294
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.414705967291963, 0.2, 2.534446876515746)
    albedo = Color(0.5968826505352177, 0.7097111720868758, 0.455841743232462)
    fuzz = 0.025169740786023964
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.180000171359903, 0.2, 3.691233117738927)
    albedo = Color(0.7198677808000229, 0.011661667990112316, 0.35804600283728355)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.371176140960303, 0.2, 4.480609665076599)
    albedo = Color(0.5138628070596916, 0.7592312968648374, 0.5005967429867874)
    fuzz = 0.41136208937739394
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.134058482451556, 0.2, 5.431927440157547)
    albedo = Color(0.10632642074737488, 0.006738709594182041, 0.19468365093269308)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.781467902403542, 0.2, 6.548236512009559)
    albedo = Color(0.21577071832807498, 0.002027848739548889, 0.605757749058241)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.092272352105195, 0.2, 7.732475872271392)
    albedo = Color(0.029044278883661387, 0.18813486822868483, 0.2732341312471014)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(5.6473825573947325, 0.2, 8.7420487580312)
    albedo = Color(0.3244283567221606, 0.5509184941075336, 0.4401525385486404)
    fuzz = 0.06653998209912032
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.291068180289293, 0.2, -8.16844843825582)
    albedo = Color(0.49241722416689265, 0.035479607922948075, 0.15265557242479866)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.234218685121727, 0.2, -7.352069522121287)
    albedo = Color(0.025645899831210496, 0.5876443971401719, 0.08634422374111)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.430404743136925, 0.2, -6.82383463513727)
    albedo = Color(0.4474464243229664, 0.5635454409548641, 0.5590531235444205)
    fuzz = 0.07361215184720621
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.6600546448690725, 0.2, -5.897788931559551)
    albedo = Color(0.6233460890519968, 0.411015022168166, 0.4512753960220061)
    fuzz = 0.40699250404119
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.409360011056525, 0.2, -4.5572147477127505)
    albedo = Color(0.04113835200773356, 0.0009144150424763733, 0.553560341410347)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.13844945112122, 0.2, -3.324192405284321)
    albedo = Color(0.24552859165364874, 0.3758417791560762, 0.03420968173689919)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.001970307831998, 0.2, -2.424150652395716)
    albedo = Color(0.5802522463419092, 0.4945307029161603, 0.4530215682489803)
    fuzz = 0.04285536496592335
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.119449620001834, 0.2, -1.894563617486764)
    albedo = Color(0.11990940707724608, 0.20047188188305223, 0.07212616214291019)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.718466392067054, 0.2, -0.8288608260087619)
    albedo = Color(0.046018208594944425, 0.11240436190759176, 0.16646176031603724)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.6265967402379395, 0.2, 0.33158497123339076)
    albedo = Color(0.42747940211211566, 0.6194466501412935, 0.6213545789492645)
    fuzz = 0.26464502102306686
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.387490265213259, 0.2, 1.6510474837866354)
    albedo = Color(0.05471885984171388, 0.09979824617746744, 0.08952911657491022)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.040591891940532, 0.2, 2.8498973952896036)
    albedo = Color(0.21129722995439842, 0.13069876443483724, 0.281131003893074)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.483997664750082, 0.2, 3.4840316558897664)
    albedo = Color(0.021510770508563967, 0.028215844399264462, 0.00494613602441254)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.37789741619741, 0.2, 4.026411152500199)
    albedo = Color(0.13246949897317853, 0.003917933150813148, 0.06058023449172079)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.5025428619397685, 0.2, 5.052641221842376)
    albedo = Color(0.0743425946122511, 0.8500477937398768, 0.0697715789396911)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.146663928815293, 0.2, 6.559131394685034)
    albedo = Color(0.031934985758066525, 0.4536833113614914, 0.09802288344071382)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.616523779007952, 0.2, 7.735875127496716)
    albedo = Color(0.018840227036476684, 0.36168977238943, 0.256275528616021)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(6.198627959485077, 0.2, 8.86300134432133)
    albedo = Color(0.07202761886824983, 0.523064371586261, 0.1474827187933739)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.4943508729636115, 0.2, -8.394726397936603)
    albedo = Color(0.06502928812959588, 0.15831175790914337, 0.03954154421761122)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.274370929080537, 0.2, -7.320064808603552)
    albedo = Color(0.4864252016167286, 0.37210883814986323, 0.480819062845515)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.12096947590115, 0.2, -6.364995711461374)
    albedo = Color(0.04686876786412243, 0.16331388167566652, 0.05605901804169197)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.7759830217632695, 0.2, -5.41783915687239)
    albedo = Color(0.3117752404642065, 0.6495863243397133, 0.05936203778741551)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.78576601444929, 0.2, -4.381850467910267)
    albedo = Color(0.0510368161785762, 0.03787315817255467, 0.0880205920678056)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.634704752206966, 0.2, -3.2270690605184726)
    albedo = Color(0.3052632911930951, 0.4039181935172858, 0.43406834538122946)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.867087990419373, 0.2, -2.8841917870762086)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.279556454286722, 0.2, -1.7039940697698763)
    albedo = Color(0.5133784962143151, 0.787602201403743, 0.23615537298462438)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.411425269081804, 0.2, -0.6437160229783142)
    albedo = Color(0.06179453406804983, 0.14112194493300334, 0.03246037631447618)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.176583743548608, 0.2, 0.8880996627366399)
    albedo = Color(0.46589252547077903, 0.3915528960482535, 0.5510454031205699)
    fuzz = 0.1921229403125656
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.561582415947436, 0.2, 1.0432356293716984)
    albedo = Color(0.476961208741049, 0.7033189828079888, 0.22150003852568176)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.80852431074963, 0.2, 2.6047657176942027)
    albedo = Color(0.5703113275234601, 0.6249044080789337, 0.579347647643753)
    fuzz = 0.4308171928085377
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.157677930029057, 0.2, 3.0189352771498594)
    albedo = Color(0.7058107625224442, 0.4133373812779142, 0.5138895196037114)
    fuzz = 0.4464769392013309
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.644633152538155, 0.2, 4.7910588615789615)
    albedo = Color(0.16541202042830377, 0.2945708640800993, 0.26010793947212457)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.010279644378518, 0.2, 5.453135591611814)
    albedo = Color(0.015154091873114794, 0.17841452716527528, 0.05281218688133817)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.4701312593794835, 0.2, 6.183863283257827)
    albedo = Color(0.06194213439447122, 0.17303997125719017, 0.45700100724210513)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.751698899239037, 0.2, 7.790165975637415)
    albedo = Color(0.07201976695939544, 0.0329862709720199, 0.7957662763545762)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(7.000884572086758, 0.2, 8.819934541442839)
    albedo = Color(0.5760535348174364, 0.4649478707879861, 0.06250802263861337)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.885588219663411, 0.2, -8.756769958032466)
    albedo = Color(0.1102658969582195, 0.7031323214145309, 0.3434300233263978)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.398040042325679, 0.2, -7.969129728812994)
    albedo = Color(0.4276386945643531, 0.004646372297360242, 0.5253076939146266)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.316550071963723, 0.2, -6.458909312329991)
    albedo = Color(0.37282922058157714, 0.4294268675500567, 0.6883627150352319)
    fuzz = 0.332025040597948
    sphere_material = Metal(albedo, fuzz)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.310959027251563, 0.2, -5.966977648691902)
    albedo = Color(0.1524836717331954, 0.3048375379765145, 0.11251902234578637)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.565812033052149, 0.2, -4.716793732190466)
    albedo = Color(0.7300306778104222, 0.38895817205207067, 0.40872305317330854)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.56704271466754, 0.2, -3.4210962730519494)
    albedo = Color(0.3260886518077406, 0.18368406953076552, 0.14626832589005895)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.72574980801797, 0.2, -2.6816424043905416)
    albedo = Color(0.16638171560135137, 0.06374989629491268, 0.5144540857015493)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.151143643987002, 0.2, -1.156273768650804)
    albedo = Color(0.23581521784091852, 0.009716928247858152, 0.19207156525276803)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.176324853754315, 0.2, -0.9645158644724415)
    albedo = Color(0.5841248881278559, 0.04504485725186596, 0.0011309945942444403)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.213866994850406, 0.2, 0.7354463323877669)
    albedo = Color(0.1385283306962527, 0.45888928306238114, 0.3639305532594517)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.450333357475337, 0.2, 1.718726095372648)
    albedo = Color(0.27128757427937766, 0.17052140859853585, 0.009727858457538577)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.377574653193966, 0.2, 2.5025186350732236)
    albedo = Color(0.10598869662223816, 0.17406705031041816, 0.16535098278162677)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.519449633514546, 0.2, 3.25651974780717)
    sphere_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.833263273798604, 0.2, 4.390654780421884)
    albedo = Color(0.20878327260241372, 0.1672481376764008, 0.038935114428561735)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.817770108000339, 0.2, 5.220127069674688)
    albedo = Color(0.042866728603465076, 0.09966146344572248, 0.05146178438743118)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.142722160459176, 0.2, 6.6397081714394774)
    albedo = Color(0.1463693773066937, 0.011635686048138706, 0.1957272278058906)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.252464303678844, 0.2, 7.60922464383393)
    albedo = Color(0.3501977799168162, 0.35543166560641504, 0.850524144746842)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    center = Point3(8.4586621608556, 0.2, 8.784948494102524)
    albedo = Color(0.1990094473583252, 0.38770598024404607, 0.16536436441646982)
    sphere_material = Lambertian(albedo)
    GLOBALWORLD.add(Sphere(center, 0.2, sphere_material))

    big_glass_material = Dielectric(1.5)
    GLOBALWORLD.add(Sphere(Point3(0.0, 1.0, 0.0), 1.0, big_glass_material))

    big_diffuse_material = Lambertian(Color(0.4, 0.2, 0.1))
    GLOBALWORLD.add(Sphere(Point3(-4.0, 1.0, 0.0), 1.0, big_diffuse_material))

    big_metal_material = Metal(Color(0.7, 0.6, 0.5), 0.0)
    GLOBALWORLD.add(Sphere(Point3(4.0, 1.0, 0.0), 1.0, big_metal_material))


def setup_globalworld():
    # generate_fancymarbles()
    setup_testscene()
