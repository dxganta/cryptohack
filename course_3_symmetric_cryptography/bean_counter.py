from Crypto.Cipher import AES
import os

encrypted = "5bd592b30ddb9059511a9b9186b526f2d285ddd800d18a24591c9b9ccf4421dd2785dce563abde0b2548faebef8d10cfb4ecb09120a5f323343afee4a69b62a0aa5f196d6b43ae64df9e645be60b6adc53a553b71271538f319524836d4f38ca9ba60fbc636717cede901178cc8dda9b8a0a231bbf3f796cad712e396874ec9ea9ca209fb31c38ab61c84c233a4384740c522bab394ec5aab6f1147628b6e7eb47722601e33915b89fef59612a8e9fdc6f621981f904ca806ea543a3309f1fa6f866ef35e72b7d176465d60cf1fe5d4be1d5f16b990a5d9caa71c035005cdd7e107c008b3f6ef59091e9120b994816498b9e73592404b4aa6d50f1d613d174da9d1c2dc9d94e0b2da2e968e1a49c2f65b92b552311fa260c9edf282260b1a34fd51a9799bc37708a63c3b1d3ed251bde1570130bfd0840ccbebfe4ce31ae28dfae7f915ebb2db4809ee1107394170d9206fa600be124a6ec0d65e5011dca0d1f4c3ca3ca954e25dcc0f4d4e73133389c3d30ad5b7f3ce4e69f8c60fb9c2239dcedf4037a686c55b96d8e3c38de3cec6736b4f47d035f86c33c04bc5393b5816dffde820d66ae551c6f362a89e03719897551a0ea2edf18629ab30a40d9721e2b04dc51a097ab0a10b470622d59012c9b0d6c92ea4cbdf36ff13da8c429d69d482379496fee5c08996878427942e8898a83ec70d6324679c063ad0a0db3c22335e545037bdf2f01ef0728b3f357fa79fcbb42d4507f9a74560defd6e82abb835d79056f2e67d1c8975b9e5e7885fb306f87f713bd4ba8be345323d34cad1476f10b21f97f14b21bf684c0d2929a3dbedc9576a79f9123ff4a733e8ace34aef77c1e3f94a26bd3f4e75c2a2f3885eef38ef8c67a585eaade0bbec018cd58ab0f8a08d0a91cd42406698b8a4a1b41cc84f86149d617ca7594b4c96935596b76f3b70ddb0044d6ff31bde77f6c31b411db77fb4a75531de877bb487d05f90a57336704c8b12cb43453d2c32d8c7361c31e5a68c53122db7f562da494a0037483064d415303c9fe5226b61ecc5107664533dfb608775b406dc9b7f10912005e4cb092db5214b4ae9ea3c2e22ee9f7eacf759999368ce152892e172336dc5a079d91fc3663c34dfbf4f9a185e4445514be406aada6afbba43fa537bfede2676c51bbda572b62ed8ae306f3f7506eed1cff88da48fcf5979f6bb137e020da28bc9323e11e16085491ebf72322ed93f31180bc1ebe08aa8f5dfb2d560e4fc09bc6c6ae16ef2412e75dca768389eeb91a38d4ac4e370d4e5a7e2212ee4ba3f2eea564d53560420564e438e17c3e7ef6e9dd5b45376ce3b2a21a18d876ac7fcb341f8133ce6e8e75a5b5f7ae3a5d2c0ff650a80d17b7f63065f4f3ef45c004dc699756fcf913064bad6e8a82e3607a892b1ae1b8168e63c5d5da2404b2cc978b7b2a8727ed6f6aa687721b3f8915a404ee618bfb8e3731377a684a6608ecb67a67b5b01960f5e9a1c5cc1fb8ea81ad96ce967e39a0430a3607f13a5c01678fd7c423cf999ebfffe227cdac415178634dea29ef7b66dc42928934b3c0a25189456b9d86e226e751bfb72adc26762740aa9f74abba2dfafdff9e6272f19a2adaec7543b002dbd324cf63334d46e6567e82a9aaaaa586044cab6fddebf33a954082325fe5904e78765c780b4d5344148352f3c03df4ca947ff1502bf80cc18eaaa4aa2f6616f14f2d7cf1249eacd4c6321a5603b3a202071da1e8d29caf8fa5063e0461318bd7653ec11072363efbee536909aa9ad4da5a868e6c3433ea8aa7bbdd8663faaf876c7b502f52087955b98cc87884410b1fef8f6a78896656f7ffd9a26f65e40988d10798b1d0573472f48974328e03d0e20602c95ecb72aa94931b9750965f56d8bb657b64074d63ec2c656568c9f77e9836bcdc667863c36979ffeac90ff1eb73470ff8db7bee4af0de5f9eb7d0a9b8387bbe30e13ee34efe8eccedb92bf05237df7ff908c3f3ecb3b14e4f0cfda0da319b788da80a99e72ba122e2ca1d821327d8dfaad18e6c09834dd2f6def2f40b158769d4d7e2b51810725a8703fc7d6a5e17f6f81d103c6f34fc8fb1d791309440d0ebc99e9dcc20720028146cdeb651bc89b6bd7e5299d7c11f2fd2e4e263f73253ac12d8d4070cc03c312da5e5c653c598539f046e5b12b2e5eeda8f770abe1d3334cfaf988190938133ca6a28476afbf278dc40446d284a33fb16e10fcabff7453343dcc43c6292e8fc2c83377ecefd021df5f1be9a4329585d421f5701ae0e215b35895ab235e8a6af1bade4d7189ae86eab5ac6e1614f7d2738da9d0cee7afa72da6350d80d591074f39439e82a7b8a224b9ab01fe93ea297850104efd0757b569ea64f258507438212147bc60093e2b0d040603d64a31fd61c9aaa4c98689427c024971c5fc3406f79d91e152f3debfc28af3c61c8fb61be9982e9a1ecee480540b08aa7f40b4caa038e46d84ff19b2c5e53d190bfe712404dc1bcba14d08f093e3106d3ca86b7af98b43c2bdbbe1aa38df6625a227d4d27477edc9793eafef66e6c05f19fe15880c3588e46f2d8aa0ec6b347f0ad05a812c1dc7b673d8db5e874414dc99845a342c04651d27b44890c0d262118a183d5b1726932bc9b0a851923ec5d9196869eae169a0f24aa0c25c52998818b8fc1498eb5389f8b9ea0e2e1ec1dbb93993588d51d2304eb67105b771dac207219751219abeac0df62fb0485f4d11b05dc710ffa23c4b7d558a99a2de3b5d3699fe74c5f5dd0e39c065e890db8e41cbd05a919d6042cb91165ade5b1d81f74d6197b20556dfc89a765e1323e0efa8126ff1b8858c155edffd7d0874177de0291b5c7d69c839f4321469abb7ca68bbeee76fe26ba48e912f7f03f63e57ced5ac4e4aa7df0e2de303cec712ae5d3f4e9750184b775855524c439fe842bd077a31330b7f69deb456eb5a3f84c9df5608e046943c076837dcd6dcb220feeeca114cca8115bb80dc9b3d05e330cc75094c5d05c491a82e02a125db1c6337852a968bf8465f303ca4967ac2dc1aeddc6b6bb3930747f09f468831f69a12b8f6eb13dd774dd38d8b2924a4e931408b3b2a5f7d79c1e10eebf73c8d267b78425c307fb423b4aa92293905427c4c2c0e9c75255133a8e98df10e3c201c11ba2b336261968e9dc31736b9ae2ecde4771df0c6c53dd1b8a43a0061dcfe75640b6c2ff5da16d926eab4130acd4d7fc4f0ecbaba3c2b06df4b9549565a75b94f657bbee9ac78f2fcc70959aed5d147053e8ce97151abe724159074adf8d5d9e873d0ff173cb20544828ddf750411e40bc22c88650366ff1af31510a89a081d550b0f54aa98cc41621ba637199c43712e674927afdc0bed6f15f9c7cd599e7cf415608f7196572aa7aefa03974f5bfdb9c2ed2fe0910d33f50526ce025c59c549cc13bce8e076c9f2d261a505e479c6d9011d1fabad94273094d89a0600ec0a4d1c50001f0e306aa2c3fda733f8fadff01242d3c522350ffdf4379434c4e61c2b99eb6807bd1fb70c39e047f4ce099ecf74d4e6c184a0d3b97ea7f67cdf02c8962859edf405b5051bef56a66bbd08b61599d869b14016f374bfb22151ceb05336af890d8da433b0a6e2749763c27e385d0ea63f4a88952be020dbd73e497f2b7e19f67ece7e5db5fc8621cd5faa35f6ad520842bc8f1f6e7771d2b8b589be41b0819ec7d767f3f29899eebebfa7a1d30ab0ca410d425035326c93e3f8d844adc8bc0f3f02f8d6702f1fd62ae213bcf9b613500976b847cc4f912dbdd14ad493b6102ed71172681bce2e830211dba67ff6de9937332195cda93afa6f5ea7e1afce1e06579caaf6459b4950989caf562e850d1e96032a020163c92267e693289c6a6cea8e3a44a48d2e25f286b8ed74db28a382329fd1d826ce3ba037780fd3bd6103c969b5b7609ba2519f2d010473cf2ea85286cc72a6b298978e4c8a60175f520dbf052e143c5e322806672fdfacdd11011459b70f3e99140306e4e01a7ba5df0f14ca0c3438d3d627ede8b93b52cfc89cfc4da5483f799b2dccacbca87ede2ec33c3227cd964822e9c42aeffc7938cad08c59bfeb08bd2d55291f86567647b46ba682a10702bbe929983890c7d7593617e800b4d10cd006ec70c8524a06d2b3fe4c7c2e27e6fb26b7bb7164650b4094df3e4f8e90c9acd5c781d87817dbaf3c8df610c37e22ef8b32a78a16cd9c56992e8d79a0469ab1ef1fc298438067e6fc9ea95978e414be255db27b361efc6598cd6f899a5e24d0699974c0c74d77dc880ee8a0616608631d5db962b7dd9c36e7384062546248b9ea6399f2bc237d10da857c0a728f1c2e26c64f365bce180273b09e4c11889dd76d4f10308a18547ece9879d1f2447918c661195ec7f53b57a02066460f24f3352fb83001c8e97b7788f0492e2e0431f66b3dba2b14cccf5d2da77460692b54ea1275f1040f00a1f02c3ccbf25a70e4713fd4ef91c047d18f6c009f4f3e08cfa11db529618bcaeb6d801ba96eb19f573dd2b245bc1d9d0c7110355ac4b62159e829270334a072cfa73de7f55d0a136de688ad5d40d1a3621b6bc05f8dfdd3867cfccab228dfae7b0110bca1c575b857aedd76dddca94f63eb1d6229c2af923dad6db3061c00b9a072f6aaef1cfbb16ddbdb55ac932cc187cdedbcead41fff040f505d84b5db3f97fba62dcd7bcb69b045b646d06791dab9ae896dc6fb7c05025fcc0fbde24a7db25701ec34b7e49a2945701d834dff85abcbb625f513ec13d90bcc6d7fc2add8b6d881a9b6d04d40d0b483c318a7be53564f9c615f22ba2258a725d12a24d414de887b6a21dbc52387d290255feeabc686d19038e8193001e8fcf3fc17d47b9417b3a71ac143c1618502249f481d033ccfc2593f0c8af30f718115a9c36d692b3bf0869f3874da9310e6ecdc06aeeb8bf6a3ba46ea789101ee04afa13e477cda6e5785e2427c5f4c8fbc0289f032a5493351cda130d1b373c61e9b5a20a9bf0724174cd18c637f43530bf27304a23af9b4071978f505b35e479bacf511568a19728200463c5dc7e6217ef3317f24f8274123d299af06857290d561212ca05460d5743ce5e8b6c9d58bcc8ad25201936af1a81f4885e7dae7d9fd05bc9e11b5af7a7db74a10afecf64b90d9530ea02fbaab8faffbf2b5c6235951d7376680ba62a4584a36d9c9efbeb32817d27d2dc2160b1e23def36d8f34147ef5518e2c0c5f74842639cd63185b8503bf0155aeaffce45399c8c51bb6aaee504a3f39d7dad22dde828e53fa5967a056e233aaee0141d608a4d688af97862166b466783fd17296d4cb631ecfdc664ac973953ee503a6ef085a8111396696d05fa0fabaaaa052c54cab88498a3f4699509110a5d98980f90a561c1ae2ae6aeec4474c4d407366a85cbd0a4c8ecc5c8a07aebce0b699f298b7e6697fc8e2818d9b8489631b194b67271a3f005ea7a2ca0fedf543833af089c49f977a329fde4372a95023c0a975bb9a32443c391a2d803007b12069c33b9ff16c3da879f42f759fc69dfc99777781e1aa3c627be807991108d721926748c871ab3d379e87318a661586f24e02128df2a9d47092f37d5f4729b99ca30521ef604e8ca8ad1c960e1292c8beea81987d24335e5982ae167af9f981eb092be3aeda5442ce976dbec3a00905072cc55980525f251f1cda19c429a5b3b41f53757e808cdc1f1c473aecb8583b085a602bf0e32d5338eaf99c3745bdc004f9e1343bebdd1e27406bf06c4f3822b44964b14e73c801e8b47ea0feca1b1286b1234f5abd9d5183f3c8b3d2fb612995095474464c20339927601d6b985e246668e451ded8f13cdedb4c18f225a50e3e995f143afbfc3b73dcbafd8be96c5ff72f4ba7af738899c98e9bac912f1479029371b218ac18962537071df309c0de8644e11b95fa05e118dfcebe83bd270cf27aa936aff1ffc48bd762de7f2eb6812abdbb652db9cba0dc8311614f1e44959c2f621687debd0fc67ef5f91e96a06d33f8bc639bbd2fbeb9eb2737b204a32051f23e86caa699fe1abaebcdd021592c36bdfd36a4c87c83ed6207d8bd3b8da7287bcc5cb3d8004c3c251d7f391f5a7ac6b03cb4b33e17e5af3fd49a7c1123330509b8c71d5b8814ce4260a590e75a45f0a8f5a4f0b5347669e2873005b4c68af94fb183cc4af495d86e7280bbcee671b7636b4b7e9d8640d44ada19bd3ce96190c82df30f119a9c83583ac145d4393e1198bfa469b7164159aa85132a89677f0a2df8f6001289a64f460b38442645e1a3bb0867fe3a5d7a0edfd040236cd9ca5ed4403b0c7a25f19c5a65bcd3675537ab9480347359cb8d285dcf2629acd17511a9b9ccffd9be369fadcf400d8fa1b08699b9ce1de62a0fca6dd8ca5eefc53511a9ce886b027a73686d8e618dce098dc539b9ccfe416e58af19f9b6dbcef3d251ad8eeaa9c16c5b6a5ab9d74b9aa141857cbcb4ef375a0d2a5dcbd4490de2b8bf706e59fa9355a253a6125346c3ae4e3d031541d4f57e2060dfec58615ae4bf6ce128f889a70ed5e1c505d4c43b89869b32aba5c39f8c4184ff87a2642d222fda2109667ddca18638cdd9107905c35b8bc00f2b5c48dbf216e277674f2c1e039d43c366469195b0cf6424ae7aa452a9f69055fed7972f0fa9116b7004a10d313bbcb5d6dad4ab4f8ddc8fe85db9cd613bbd7ef7729663463e5ee6d60e59022ae8696170affe563d31e912b85c5a00bc573bbc87240dfc8b8ef9e9763f2de794496ddbfbca14ab490ab4b37cd1c877f479181108df889f1bb7da1897de190de41129f7c3e85b11e1e01cc8074a56ab19491535407bd1bd9eb91d6f10cd789209fd81e97fe8694cc6a3c65251f48c856ba4b3a3b68fa7bb9cbd5f4e078234374b0fd7cab227a33ca679f654db9296cc83e4acacd4e79e6a4ee78282770a3f8319b340ad4efefeb48ddc97d76f57983050f448588c5f8748d88718c00084a11c8c08706114d7f60047423be3786dc825d5f9c2621f2ce9ec363dd5f0a4f70da922b1e1d1ff2c05fc8bcebda63fba1765717b98ab1e2d0ca0a7807577f0bcff1bf609e1c1b8cd174f3a32790eea3cb0943139ce7f0425819ec75509f42284a4b33d1583adc88baa50447f460c224552ae4e60dc6c1926d28054ab4bff2f8adb4467ad06f76ae642e863a70a600f62728e4e60da101c1dbf1a98eabcb02f6279ad8946aebeccf6aa9dd3246b74a9618ee51cad79d13089e1ebf9426cdee8dd7c0f64300169a895e73cce49e80da17f31b5b9fd45510ac6772a251441ccc7be8965d29264514d432a2d262ddf00478edfa6bcd5b19feffe522a8b32bd1f45a7c9c6e6c27cb371a2d8955b236058470a10af0f2398780d3fb3f6380060b1ff5e190deb9f1705f728695d03d5be14cb968cbf482bb3433005f6dcbe6f0ef6d4c01e0e601b3cfcc64288a4f3d82dc0478edb26b695ab78a8cdd72ac894b3d3e6fe313336102bb88c59c05c7954056c6bdd521ecee05565102d5498b91fca5cd6abbe08383c8990181faebe4d0aaf3db04d48f727d3697ef2931e31361766c79417cdcb0b7d700f4a597e03b499e3886398dd60ff1c972cc94a6e95c2ef94862967334ed4f300e96b98b14d0a3f41d7605da7abfe2d559590a787317782ff628baa48129ec049a9dce75e82a50c5fcec511261bbb9da1687f82db775d7c29bb3c4164d6082eabd0fc670ef2d1a4a13734e76c933313affaed6c7599b431a437ba273a807044f3a3764f66021d2fba28a9018eedbdc971e2370c29adc6c40279eb58b9e4547b83d3ac9a7cfb6abfca55caf7e0d17735bdddac937a86a548ddc7fc55335ec6eb8393e2f1d8290be1868ae2dcb90490148c91e3d0f107407507d57a3d20e43e9a0215e083a65d334499db044d58851533a8f9608d85af47ead0fbeb065d07e2fe462fb53c717aa8bdc851ce8390af4f63dc7c0939d0dcf5d3b62cae4376cb195938894c4f6a1339dbb55d39ea9888d8fc4cdd944ede00a78af302eb5da01447e9c1413c079208198ce9785f031cb37377c393b68fa1e9ecde9eaef84c13a8a3de26364c3675897cd3eac15029f156ddcaff04b0d26b9bbecbbe2fb6c99ccf040cf4e49174a0dbf580e57456d0abc6fa7c2f81f0525b775577a2203bf1dfb14165d07a3b0e38b493be56f2d105a4f43dadff3f1a238efbbe5f52a18597dd2e253714d308e851a181795d9495e5e38e1636662795815894b91e2bbd3fa2b70030d46174a19abe9c219622f45651a9cd7d69d94c7e848382dc9b2b214c45899eb25f3899c0f32adaf802cc8f4a08323c3c88312ff0873439eec9bf7a3ae1548d65afb73748778e552228e4a356091ef367464637dc86158d5d8a4fdd55864e0467338b97c21136cbe5d8269ae8d6b3069b5fc7d7e2324d1c8baed5cbaa712817ced9a82afa9a50ea8aebbc31aee3f9ada1572f7f08bb629abea99d2fa1fef06a0b6d5d8ba5cbc443393af4976cf36493b65583c4f0e38a7c5428d6c2d6ca9f0297330b196d8d23c64276e0ba55d8c07ca627d59520193baaab9b1c660974629ebe902dadd8e75ea28ca67e4c2ff6a29f0522faea92f8d5a88fcab1a87cfec0da3a16aa3a7f43e0a94306b014fc8184392c039dcec272d4398eabd1c39cddc548d8f5971532a8f73bcce090baa7bdce0e64b4d35c00e6c41e7c293ca7294459e2b2b60c170ae30fc9da95dc4d9ad8701d1d318774778f25b99ebcd94bc409bc059352882c092a0a3c263550921854ef5ad4873f2f5f7809894c68fd98c3ccf942cadeb8a6985d4f6c9f9dd58e428c58037357ebbb1e2f0e321535d648523c7a40f597dfc7b8e83f4304295d8f1055049b2b1da1a9ff787968850075e44641898d81239ad07c29a05c71e19e5e7ed3c67fbfbb0d9d98af80c7d6800699fd7f3a37a58a42522df742640a03c503bc4b5b85e48081259adb927e5f3a1f8f0f92873eb28e9bd4f877a915166326b17e61c11bbbcf7dee8bbc960a3d182d5f68b14e86d6c27a654013324f785928a595a548f58475ab78afcc0de205285240efa13ee6130f545210737a8622e7c2fedc1cc02eeec27797e2ded7fbd5f6b329ae824f0cf6d63899dcefc2ae99bc494bc889495c5884df331f1b02fed9ace973785da9d434a011091d4cb4281f3e44cfc7ba9f23387b6c2ecbc8ee1e671c492ba0eadf62fb1f574136f5d421a5e032e24c0675ee8fbb2335c360e8501016c6c88f9a3a60be11af5f2a11d1019b236053847f19a736922835759d0a102970efce68981d1085aafc1f1369b9d974ef7a88044b2e9709f84a61703312e84f4a3be01ea041a9a356aeceba8dfdd59aebb58b62115e8a2c17bbd1b0cbc22e0d2673e1660e31303014a1b1a49fbfaecf42e4921eb2422fbf95adaddce811edcc290c9f177a6fdd86c01686c9e5c3280f0a7de86b9cd04dddffaeba4af4c3ac0615c6c47b35215cc4e8cb5c1452db2f094f9a78f7bfc5c0e710aab5f860e6e3b4f18c11710667e42591ecd1ba2c7ffaeb7e0b94c723480ab2d2405e42df4a66614c7fe65801cec6093d1fd2feeefebb0cb9c5591cb47cb7f4739b4b3c0188745026ca8d77e89c6754229cadd6eb16961386e37b74998833d8ea4167c2f9d26e59744052dd93bc999b6e98a89da78557eaa86334afbff1c7f08782edb0f9fd380c28dfce40801538ad8c647c07745dac02b773904f12093a6a30e12d84d049147f1bde4ec65b4ef7b7a3118da6c4c181e802c988a7eef90484a0b8582410d92d079cbae47c84917b987765b7f3e1d854755356cc428c5808784cf3a277486a0e3e38dfda4ab04a27c7e5de2e5f6bf20e2e2ea02c8abafa345da1f12d84d0d92d056015854a2738846440f737122e033f91fce558e7baa4bb2215cafb7835c2e08b2949e24d30209e9eb20b388c5851bd9134e179fd848b545da1fecebb839a567f1abf2fa733746e26bb9fe92ee4dd113d1a4d8da2efff2afa0dd8a8cdfcdc4a098bee7cf04d48f726f24853162504a88fac5a78fbb148c3b6500cac390728042b0752588c4164d909ad1f0442e6d3b2ceeb9e058965e473592cb4a8dd1e37c1061369faf5bcaf0292b9c767516b7d26c6d108e5d847e25bce1ffaf93e09aae38d3ca93bb6864d007064dc070c2a7d837802c98b94ddcb0686afb7176c5ba25e7e81178b87ddec1fa05b8222556ec40319a711cf3d3ed66635e59ddeee176a7224d1ac3b643924dbfa97f2ac4bf8e11e3bee9f0887dac13e350a7c5a32ba1d1132f73312f08de852c31b21bc57f21bf7df31494ea284d449d9f6aedea49bfc310e8a16ac1bd6c373b3d76ff0032dff3c88a7e6fac2cd90f11e9a1205f0e3c635527700c9c3487f10bb7622c5201b33e1da89085ad5941c0f6d991101f487aa538303cf460f1e16e26fdcff14d1a2867be5d829bb3474aa54e602db3aa5470a26012a45208d1f39a5b4100811607352a3ceffecab1459412643e04a8dfa9931aaa578799b1453963ba1066e7a0b3801fbf0a65e4e80e95a88252cd5d0532ae6021d2cf79e65a7cfc01d79ec131d9d04f8da2f5ac7444f39382c1805c7ffec3563598e06d5884c1e2674bae2e296e50cfad174019bc4b9ac934363dc5e42ef84687f5b6ed85141b1e5ac7238147d3885f90c0580a4458fdb2686a416eeb4245e968b446173f0be0bb6299d756593a16b5314611e8dc88842584f2bc3d9a0a38a7a8da8d9c9064f516cfcd5c4f872b8fdbafc6335d1369645012a8bbbdce7f71248366dff14c5c3f02709ed724b7483ed33a560acc769a4b902faee76c24bc1a6c8af8afcce81c5da708e77a4a3e8a6557cb04c66ff29223825c58d758a9c17aa18c171d746a025a4f51ced52c557fbf46b2f3a3faf273364416084382d685b7c275b882d1694a9bc0030249185407b5ae3eeffe8493fb2c6f2fc10a97c064ca3b79e44863e18f1691860bdb1af7c430bbe1ff50734bbfcefdbc8f5ff6f1e2a948b516e7ed689d4cab41d8f2cb0cfd801ef8ee9bd3b6a1c18cd05067e6e1dc175e1607a9cf73c35015cc4e08898e1f2eb1232e79a040b564bbf18ac64710d4ca0ce0f697fdce3a0be033fa2f84524c872e24c2712b03a36e354c738bf34e5d0c93d8eebde5cda16e35cc181c63bc034050231385e26b6f60ed9533ab7b772476cffb65670183df1450e63a4bcccb4852dd5ec8c253ea45b2e9b0d555b1cce7de708c61868b5bd7922b03ddc284af1a647784c08cbe9763e0ed9d4d7c2603915205c2474f163e10cb90d928e97d1117340d924b250d9ca00263d5fc8d4af44bb7c72298205e47b3223ae202ac8fe74ebd62afdd8a74a02aa5fc256faa075c309fd51a683f0c23d7d6c51c1e9165a53c99a45c2b762d18b31ee8a0b7d7c323b1c076aad73b271a3b8d32235027a6a17b083206accd3410e4d5c51c1e7c11227c4e1178652ca58ebd79225b145fde346351fe148b37278f1b90cb12d99110dfac9e4143b2d2f4e028fda637cdf7a5a2f1de7c7226722b57bd6c9719f4684366380897e173d57c53a7d6e43d3f8ad3b85cdf3ab25b0155406fbce716064d4c2c4d9850390258017996479c4bdc5c9f98cba5afaeb87317cd38e94a9c9e15500be0ba30f2c0aff7df71385876652dac4f91eb074aa9ddbe4518104b92a1ea6bdca2904f0a792e45c025079012145f9e22330f294c0e3ccf534e4c90023dd5dfa8afaa35f716431a36cd1c8716145f333764be17d5e70f567e10cd96dfb9f2f3140a1f73ff0169704b773e54f394cd6c4b905c32006c3bc2883eced40d0f39ed7454425db68d248544825308b3baf110762597b677058a27afe9a5b08786cd383261f3bc7e0c8dd2fa7eb1a2d728d2b60985ec74b6d40c9876e637ec27276cd5562bffe7927ee52d0d7c95ce177128a98ec2f06f18a060d6ee1acba66dcdfc579af892bc64072e8ba555844f973f579e6a390bfa9ba5abfed72380dc05d7a627a0934410a527702964cb34295d013f1f3c794b74255700905e962a63b8ba7987611123bca8db8ca5940f1a36ffd6d57c3f7446799defb88aefffa1493f561d9cfa57a63ffd5f3960c834e6bd08ed8ca2ff2748097782d881394c83062729d67eeeee6c2ab84ddca38bff65c0ff19e31e965924e31db040d6f005d4ab606209bcd253bd27e5d7d1f6e174eb97b0b52f7c64f180989446cff9669243aac49abdb79f4fc4e9238eab5b3560117bb0966b7744fe75a7c296c29bfb8a1c905ab784def5a6d410d3a154062e0a4cc454d2db9b219172fc3ecc91cae222fca75e5c179614457720d8aa7ddf1fcf327bb3b7fc9da3f0c236f4866506416bb9e23bd1503e1e895ee3e671c4b39b2fe2f6383e752ca4331f1298da8bd2b25283986f6d260b0d5e7c9654a659618f97a026b8a460f3a8d5c9569432690547489ec5d4de95940ae1a0e86012458dfdb8a8c35d443051c8ae0c0bb55940844068c050888a6b734cee01859f2dc489a115b3e930b0ff7e99d172e50e7cab4860943158f61aa2e06be1631c5abb2986410a62ec9ecbc8be878d5cf26930154a6206df0dd0e4714cbeebd906647389baf002d09841430a8a8d4ece056e722f76fe3248867d7f34737320ba17d5e7ab804c803d663f9d81ac93e6d44bec240f3dc42ff800dddfdc4a3f880c812fed276d4511a26d9dd442b71a0e9de2fa7fc39bb30785a0464309880d53615e84a70b051398451ed7a7eced603b2e2d786dfae3ee1acbaac49a3b0ed6aecffb7000575e6f37bea8787a111f8c63a3dfba9913f075a372a93e508e1cc37f31a3387b2c756c39a2ac9dcc211c5e0dbf3e1ba408552f31cb0763c8566b6d3e3c490f6e07f9bf965de2ca5c915e1e87d920ccbea9d8f6811c4fde92fb5b4b18ea91471dc292ba0ecd974e4001809780b2adf10d0e1f156017064a09a6e3add3e07fd12871b59064b5cafc8659344b8c50342317e7bd15c254d2ea233f0db096cfc041e2021fb560b1aa05fe44968a4438467fe9f63af8137d41b221da7aec2f1887953e2be6121e2010663a2ae87a839904c6f0b8e1e919c8931fbed3fbac4f3800c11c19e5bc4e9f4cf114917b7724b6b5a2809bd13532e68e3c3e75a7691baeea2a58c7b1992d3b60b981c4459272a36d118a89c3eb1fd58c5593cd4ceb876f5fcbb060321a8e46d52d4801adf04fad4a3c429ce9f307d6c2f603121ede4b79e680e0b7ceb6a1a146901d6decebf30ca6b3da8cd5359deafd030e45140251e36aa4d07d260e22e5be47afe465d0956af380c00cc415b8a26d5dbbf071049ffcc3f0dad28ba3cc49bb50627d5518784a951091b2c27b87510a53e9a021bee1d3ecd112f2ab83831cec9094df9e2fa93020c0b2a56048bcfd2cb8f04a85f60ecf55f62143440afe2f46955cfc4f5929f0700c97ce87efb21c146eca0babc744685b6c70336ae246729b22206b03a9a42bdaba7a5cd255a170825d5f7cad34cf3d4e2bcb4c1e9b4bec47c3c10a9f9ac9f3d8461290db121cb5a9ca9869edea495ec183344945c7e8ab6c9e6d5c295047bf1bc8d7eebc77b562392831e07a0df929eb2c83573701b8a26d5dff4426160f3d2264174051dcccb12e101541ace494a3b11c06e3feb069b1b893d0218dcde76eab833741ecec0c7925fc167cfdba6556c911a2649e389dea5d7513e1d05bd3a44d319a55052d891f441dda73e7b4dbd73a63de7aa8ce1d62d5b3cc21ecec232553047720fdd82cddc1c47f9fcfb66a6453cd069640c563d776afad6a7442f2e976b472336a62d97a584fca7fed879fd53196f619729c34cbd6e82717c6c192158e4c96e4bdd572a3f8b3bbf011481ba9aac4e05f6746d54a67ac33c68db19579b0728019e2891af7195aa2fc56875bbe3c80c2a5eec612ffa47da55fda3d4dc8f25e2cfbba6f3164d05e7f8d9005837bf634c6a9814e748d34786781a676775025bd5bc15ed14b47cafe07f95705fc35aa68123caf13063cc64e440f9ea3f0c2f8405dc7d91f7e3d66bf4109885ffbf315d7a581dbf323e1ba23053b9d6becebe9314611582cd8898e5456c9ffe9ccb9be6b198ef348f0d3a871734ac8cf4c53cc0e938ba487b6db8036737a0a1bb760e7999f35653570e9968b88c316c7af09189d41d35b37e19dc2d3bad917a580a51ddf2d15592fe6b0ab4628108eb0c578906b3c608fe750f99e79090e91198df8e9e273d51d5650f99e79090e91198df8e9e273d51d6e1c5f956c5f0c10192226d55ff088b35affea65ef1285d9f6b0f78fc183c3166523964a31e0bcffe7f9f7e7aac4e08808fc224587590eb1c45b146d81d66c351dd4c19e79098e72d398aa758e8d3b90f941a8a2cba30f317a8a4f6faddfbda506246338e10143c215caf674404be24235b2b441d58cc6393360f2758f8cc18aa2167fd5ec5fbfc91557657a8c8c39c43dc9181a19f459254f192be44436e1004e75daf32a2892141378858f324097149032594f31450c8dbeffcdb24627b27b91a9782392d809bc0c5c6ee15a28fff0aabcc9456daa368db293c54a45634cb836afae77384d26e38c48f37f6238507773bdafcb125078f9feef6828f18bdcd57d44d38a6b26f4870e5c6e653db9ec1b6b8fef705b4e64633d82105d303c6bb2a8b8a18b447e445f69242a0394c8b4a30a7c154e977123a28591a33cb328795122fe67242c347fbe5250c2ed6b45aa3f0ef53afa22205bd9decd6b4cfd58209763c2104b92b3ed9582f375d7cb05671c7503893d3d4c008087be17b689b6e0b955b4659e5a5813c325bdd8f48f8dbbb06ea4783cac099c9fcf0d4c0167da856e87e79fd803015a3fcee66ca945b6763a3924e5bec7517a158742bbe977baefb6d629f8a35751eb6d6ae992dd5de47c2f6bff9d984042139bbe5ab7ab7579d2f18af7236f98551a0a572a59d113a14d2d2ade8f6c89969584037f078d786306804b7e4c029633088483804b0e799093f1aec40575801e2586ce3071eeacd005f8d327c2370d6ef6e6ea222727a042aa620c629977643fc6d3ca62a7a77cb978260164324cded224c4e13a68b7cb5d4222701083dd0416fee9a53cc6de59341eb8338ecc6eaab685fc56bb13be19dbf8223262aed186aef24a3f03808043314c0a595bd6774d3acc37bd1220bfb66dfe240461d30abf8ca10c88dae873cfbdea5719e70cfd8c741c18fd15241d0c9e3cbc49fa3b21177f8d085003b1c451cb89da1207d0cad9db901de0905eb390547838674f59d8fa35947269b58f8874fb875c7cc5b3d80c0e752a90748a8dc69654b8c60deb3c349e04991c730eac9b84faacafd42e2fc40f38e925539905c7dd2fa38e7aebd9acaa05e1399db4de1d6f8cdc86eb07a7f8a6f27572e99fd338d2a56b9bdf67f21d044f8eef5023bc7ec31203e2f60e3e3a421bdb92d2c726d4e8982f839318ce3d8ca0de9ecdff6aa0005108c0ad3de5d8abcd4d4afd2a2deb999e2816b9aa7d7d22f7a6e739f149d6ad793feb49adf6afe1f7bca3f082b8792d24c9d800356282f259158742bb904259aacef4640e342e12943c396aec6284f7a05900f52487781985e76e4638811d6f381077914c179eada7333447848989c60fd55bff5089547d846855e86252af3778a001d5868e53a8e14463a1087c471d1abb2ad407f05a320f376d1542c103513c73a2ab6472ae4e64631da327d6298e3eaa99da08f5efa4d55552e916b50ff56e0a591b233877d58a0700d3ffe26c4cb807962fabbebe36f545211c339caf67e575a02a5a6d2fa2d7ac98cf049263dd02c08fe9741d5b51686168a6569518af7eea079602e26747d5323467dd62e8baedf49d6fbead79c49037c47e7f6280e5ea0268942b55e826d579a536049bf617217a52867811e630d9303371b762302671a85fe5c92133dccd65b1e2d0aedde9bfe652f42891d8ac776e60963e9e5bd03524261cbe71ca3be11409e662477c62e45f21ed0cd70e0c1b9b217240e15e7cd37705dda6555251a6262162a3b94ce2d175a068b8e3e22954ebecfff37d9e5e376ec67c2f73b489a5e4a301615b237d3a22ee31e0bb400fe54b4c9f31fe990167edfb0fde6c8c4c07861f4104995b31508bab859b2f91dc01ac1ab34acb09dbfe2a188185a096ade368f1959b39780d500961712b35aea7c1b3b6e57f340b4f713b9b2c273db6a27d161d410f83565299970f999f7c2cb97c921b54b85307f73be3ddea11951377891674f1d7f76a383449df573347648ede35c174fd624b052a1b0ef53aadf6af118cb27b47336612828d57d1ddb3ed3fc7a170164e659f2c7dff622d8abcbb89cf30cbcefd8d1d259bc0e91dbcd0350ac204572a9f954e0fcd91b9c56ff7a8e17544a2b7861943a53a27e912c398434f0495d380320bc9addee18b7a6c94aaa8e323ed2cfb28ea98d58ba30754c8d28fc4c5a8f8ca2df8291c92027f398e387da14190133d11533448ff9e90126f4bb66822e42554c510a972b2f4c042c56d5861e06786549dd0b79ae4696eb85981c98283542a8f8e7b658ae782ec5135ec6e1a5bf4fb9f9d5e2f855c11cb4651ef9dac29e397a57a8e8d3b5038cc9d966b211af2f5a6058a035d1d3f2fb7be4de53cc17b7724c6cf4cbd0e268376a7e8a8a7f7636a149263a079d27332e21401b2b5fe9f8240faf7ea5732028e6b93509c25a864dfd82b9207ed783575e70d65a73d77f6f9092237f58766f2bf5b8a91c2987e5768fbfd30f98bbcf501df67e7c884690fd6eaaead5220f757131ce9fad3513a44e234d0911720772ef33a0a4db092a82e6102ce31d73d5bf913ce4ca92cafe904051630e220d2d787af3b7c663cdae0246b11862ec85820b7c035e4bba43977f629a606fbae24fab48958b24b4fad72e5cf42fae161523a21196f69ffb8471485a00705447eab62c17fc3e1d1000c47a63e6e6a328866fd1266259a8a530e666a99bbc77fa0f2bee76ff1bec6973f252d28303dfc226532eb6692437a9256053b2675e73916bec491b90d6f75adaa73fe633e2b3d018265738bfdfa8ab37e6562170a7d06ebac2255eae99d0fae16d1d8b5970b94560a3fa9df007132eb29464ca6b60f469e2969ef48fc23411b1c57defeaddf5c5c22c6c0ca7cc975ada6a5bc20e1940bc982af49e28fdcfe87eba322c5baf1dd5f2c7ef4dc2891c31a58e061667f8695ce5a40be5f112d599aafccebebb83a090f6f83dce7baa5e27fa705f4617446d939addec79a95451e1f380100b0340240a4d985428bfea88a93ff47201a035dfb89fdaa1bef6f6d0b6036d4c3e1745bc40690af4916fd265554dedd9807023bd4cd09a54b3fb1bc51659763a60ddbeb74fa2efe92ba0ed1ea94df0758f28197d4e5a8ffe6be4b9adb02009b06a7b873b817e01f28c6e36475f61a8d6b7a5492501d93ce2803f7d28a5153183d01323a315fd55c6059addcb124bf7e65f3fd640efe356cb80b470f0d16593ba1014191ba105385fc6f36bc9047dc71ab84879c038161411ea6ac5dccf070b1cc3379879e6a47aed8f49118eef7fcb7567a3aca258a75217864f8297272c0f27d398c4d7049ed9561aa4f87260b10def9adb6009777db858ea256e72821f94eb17af1a21c59f7966d9930c90201f83eaea9faeb812014ee2326d28388d3753cbd0e25178881156a014fc715b05e465dadc939e22d5d67dff117332c72b0de835bd15c3426ea99ce15c7cfedc9616229026794a7af900c73ef21f6aee25016dd78a8a3920d87395371977e0955acafed7f7178220476a084fc2b7d26179619fbe4623c626dfca8b6ec26f990e1a517d10abf8865d7ca34e0c0dbbd25988ae8697c3cf50089ff2d37c4fd7dee4ddc4e7d252fb50888a7e85edb467f2ef4b5ea19bc82036289777d5e000a264203afa9f91450b656340df09aa00401a875aea61dc66f3c325d176b68b191ff205eacbdc32850f62cb37136700bab279a1d7d741a536232066b8156793dfb7ff18a9b62d5a7df71029cdb00570e96b327b986a705b0933a8380cebceb04436fcebc3e8b9e687b001e8875796d321a468dd60463bf369ccff8cae996c488e8d67ed5dc95dedf1712247997bce53722ad41433789a4e6271a289a0f6e77d63a9eec019c6ee58797d9d122cab82f113e6ea71a58d4583f386b5dc604d6a2936a44bfe47d0b41c02db20614047423fed521b0ce0086918db14da54e2698201e328dcacdb63d656a59d81c81435196fbbae00d3320e1ad2c5b2c725d2e0b36bbd722f3882d2f64ad297024ab1bb448c6708554ab74761d4c32923e2d9f2f8171a28b49124badf984638f9f00425a664052c22f69faaee87e575e6af5274dfb26fd994813fbfbb0d9feaddf5c5d26d698b145d08a8d2bf1b66cb7c1fe9fad9bc5ed1989362be05706709c949d91451ecc4e552c29d303b3ff3e61e678ba326138b08d93f3b7b14888a0d519844690208e15b31eb4f0335fe2f86ee425e7eb09bc455832708786cd402093a03ffd2a710fbb01d1456ea6062e63eb26fde2a9dd0fe61e5e0dc9cb80eac1ac3beeb9e4a88faf5bcab4ada979fffba89e954e0f56b7fefac6ea2c9bfed9e1976ee671ba41b4b9cdb33bff1f1277457cfa1bd9ab7d3d731fd1763c90ec05a1b451cc7c75c9c07010c907950065145f2e71098df268bda5265d6ba1d3959e1f0e7d8e4cbe217850601c106629f4227b67a52f75891a19ee76a0b7d6a7aab38805d2724aa6228cdc5461a2475bdf4dc4d28571e254a966c03bd9ad7134131ede6e712b109ea3cf1ade6c0128a6f49606161f101942cdf8644a74fa2725ae22bf56bfc3f094a884b2a3c0af7674c226e7f86e2a2c17e79ddc14b35cff088a507987b12ee4b2e5fc18ec3d2246780e5148c6ebe96550c1fe35635eb755d2db9bdec7f164a388de87659f4e053886b43a396af8dd591fea3c1bef9e0ddb4510fece7fe5b4e0da048659468ed54c623eaf84c3158a4892d38ae2f63f57586f851471144a014518108a27f783a2479bbe6f2c8bdfb30092c19efca483a3eb0d34f5417578d614e6114b6323e0bbc25b0c1ede56e9249c44b6f3e771a2f910317abbe8f5e0b87a08550b23477cc2f201bc0cfc56b8e96b37471d3501f7195a6b87f5d0a4554ab4d8e01ef1cbfdd090bc32d03d9fd5b1e662adc8fe85db9cd613bbcb5d6dad4af462adc8fe656b81c568a61a59adbccd77912a0ba7e7ea0f11c88419592c0c82483a8dcbe317a5fe27f1b73691b540fcfa40c77db83f1068a0a81291964da14ce7b7e0f95a5c6808f5f73c414f6dad4ab3dc627f7b3e2be2e712583accc7d3f52b7423fae015c44b33619a5c7ffe0c3b9ccc0afa23a781a2653656a24182db71b4d88072aabd5b7ea725fe7e790e26b9bbf3a4fd7c8e5f4ca1b4d172fa51e968c538025834ffe304696823bab0e3f173b1c395d671b8a563411f87a1190537284a01278cdc131312a577c870696757c8623b567b6599488345da9f4462394a6aa9db44302db3f09a5bf97fb288052969b6f3811139cde9fcbf491487a44fa4d1c6b3763a3998eef56d8dc6475c280e0bb6808f59c63dd521ecee057e792ab52defd585e00bfc22c21d1f9c1017c4305eea73d5fa6051fac62c2e258187d4ac3cfe5c257cd4c8b5b86b6823ca2d6dad4a739d35d0f203e5905ee540b6b8ddf4bf9d55c77db85f1088ad2e04b7aa54f0543b9fe672dc141b7e467d101ede6e7f270182ad884428c580467d101ede5633e0c5e01cbcc41849477bf9d906de6eb12961f0019c53d37021f85a06959bed6c6afcfc1286654270c6598dfbe1ceccee5b38172f6a4216f4af764193df6c3e0c7b14e9b159b6a19d3033c856bda8f8cac1156710cdd9bd8f05f5f73cc724bffc67a5d7151590885b00d115383aca6bad4af3f5dd9a5711144f96a9e0703356508a2d94a6a68e7a71de79400f8e19900088f75a0950f08f162905f54ab3cff4d9d61765c29cb4002b71a850e6b44f67bd42205d0ad39032c8489092fb777083608cb4d8e00e4498a01e43538fd1997aa75f685d403d8460b6ed54f04ad34fefae4a343ba484e00a54b84ef09b3888c57868b657c77da4c173da7b05aab388c57868b657c77d2c882e8dbcbf2b7c039b12c1a0d285dcbd459fcefd137a19"

class StepUpCounter(object):
    def __init__(self, value=os.urandom(16), step_up=False):
        self.value = value.hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value

def encrypt():
    cipher = AES.new(KEY, AES.MODE_ECB)
    ctr = StepUpCounter()

    out = []
    with open("images/test.png", 'rb') as f:
        block = f.read(16)
        while block:
            keystream = cipher.encrypt(ctr.increment())
            xored = [a^b for a, b in zip(block, keystream)]
            out.append(bytes(xored).hex())
            block = f.read(16)

    return {"encrypted": ''.join(out)}

png_header = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
first_block = bytes.fromhex(encrypted[:32])

x = bytes([a^b for a,b in zip(png_header, first_block)])


with open("images/bean_answer.png", 'wb') as f:
    out = b''
    for i in range(0, len(encrypted), 32):
        encrypted_bytes = bytes.fromhex(encrypted[i:i+32])
        uncrypted_bytes = bytes([a^b for a,b in zip(encrypted_bytes, x)])
        out += uncrypted_bytes

    f.write(out)