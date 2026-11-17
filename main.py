"""tiny-chess-01: 4KB chess engine (packed).
Readable source: dev/source.py (6,909 bytes). It is zlib-compressed
and base85-encoded below (P) to fit the 4,096-byte limit; regenerate
with dev/pack.py. A corrupt blob exits nonzero, not a traceback."""
import sys,zlib,base64
P=(
"c-plY+j81U@|~~H(L-uvNdyTD4tS`FbK8xNbK4}xdnlDlpb-dkmk8h_`|aC3GZF%mRI*h|BADs!>",
"F(*<^vFS!CV8nWizGIZ!YFoyvChLVn6`74tyxhjZlSDOFKAM<S^Oo)lej%+B~fplUcY$x>CN4XH=",
"pl5efU$=l3an+ZMF?cVri`_YV|tsX?>=oV_2Pz(Y4{}c8qfvKY^#CwLa0%ji#Qf6vGKga*q^~-dV",
"0kK}>vOVEUS)nO0|@ot-N_@XwVXR&qC<GjgFJz;6Pa);koX>E${N8HwDKd@_i-f=?Jl^Kcp9FbTs",
"bjiMx5!v_JXp}I51X7g3Z!YF2|IAI|?t0)H83UNR(58xB7RzVa+!3rK=6RhxAtq=z!Qc$#n-{S{S",
"f(vL7u3$Cr3d1El0e?7`C6KV$%xyk%P%W6x=Sc#(XVFU4G_Cc960_Si%&uja)&)F01OHzb0O)qL)",
"+@kU1AzD8Ifuu9f9D2Ft%25hUSZEU5Fl?6(wB67t@VsfI?m{te*HfBh+nVatK~6Y`6tP=Vb02R9+",
"PZ5?rCQiI>{aZ3&egQQ*GE%3fgILe`S03SoQ^?l$1^<nFE8sS5n1|Jta;`C3|Fb`-oOtnsU^*qp+",
"}GW;zNe3LTa7-Nbb!K@+R=yJp~w3Z0VAfYeK^xwL|{6rr$Ea3!CTsgW5w)CP4dK}SL|Gzfg1BZr;",
"jKr$VnIzYMZfI?+URF<ngos<rxJ82Nb5*$6;^&4DJ(oFY$ywE;7x%Aa9EbX6O`n<Vxvj{@AU(L;n",
"<}cCw+>9K=N0fHYb_%e8(fI*y_)K%=u5eW9)N4q4`@c);{i-zd*c?2zF=hrc68h2w$DlVNI&p+9{",
"=+B(AwJh)mc(TcubGTI-`Sfq1qBEMi}nX48~AC`K8QlG%%#-gyYQ&hN5G~cu=)_7J~zZem*ETzQB",
"RV}6r{u)f&lCo15E(yLPySxp3yaIZ5XxPG-a_z{BPyu<=|U>d1>`DPL0Clx+5xqM;SiKpp;lmjg@",
"{SPuYUv_L(PVQv2y->of&#E0(C<J*wwHweWOHvccWoR}L<ZZO@@-0<ZwV--g+1Jx|!;_lzN|ancS",
"fM71bo+y`t-JE!P46*$=*Ry*D2ve=^6Qcif7R33(iI^3OBZ5ViQ&uc%E+dq{1>i;dbVpzu`hDYrX",
"W%kHw#P7MYANL(miUv@Mda^9_uq^GR^uG0*Q3%ZJ1~aR{%x;Xkl5yu}jO~V7>+t6ydQB15z-i7dB",
"x}oh0u0THyJhup+7JMcZ$N&e{lx+6?g8uG!R)*iWdDkwUL6E-FZ*gPYfe{W>{~hQiRp9w?QwjZs=",
"<nq)m4~pB^%b64oCPt4^P*ReK~GK%V|<^I>=fc@yh*gsN9jP-8<vnDEO&MqeqrKfPzV)@pz!|Nls",
"yG^+qu$J9I`VjiFeN9(DsuK$OmC1x-PzjTZ3ZgLqFg2P?<qzYC{X={N{Fg@weza0TW7k|mmAOP73",
"H$yfr+)9Gg@fciW567<btPxiQ#qj668(Bn-=j_{nrk<7xW#is`h8kC&-0kMDpU)(9p&o*3u*h@M>",
"yU@-kqoy@V=&aQ|mvA^ONC}NIM2$VnDDj~Idi>aK9hX3KB;P*lzl7uKYy+IP$azW44R5-(+6XoUo",
"qMfTaA<}a6`&OkiddtR>}WYk9?}1FWx)aMu)@YrP$>8tYe=V6m1y5A1+puU9f7QK<6bhe>|<`2?v",
"QMwSS0ufmYA6ph0Q4tOKAr?5uoV|k+WTa2NFEsV5<VdT8V%WM_ueuPioW?j_TF<0JkgbIw1#^Mxl",
"$o=FhsX0XSwxQuj0w=6~Jy@Z<1Q+U$Lfy$v{BG#vXN;5C<E%j+BF2JdJ%uA%}#2YpXcC3dv$niH<",
";2ND@m(6glc$VSi#sHCqWN=w<rnKoYf_UdNMEZ;V||82DZ<EW#f&Rgxw>YMd;G|3zbLrn}fN1bp`",
"g}>$((jDwJs;JJn3UczA<0H6l0`Y!w3D;8*$UUU4?g(%jX0U%_#ddTht~KwQeliNfHLh$U#l1g+0",
"EHCc0f6K2)i8Gh$kUHO#FBOSBF~e&B}y3Nqm;2ZD_Y8eq9=9-J=r}vq*c|~g=nuiH4pVMy{dU!*%",
"i<oy0pZ8_%NIRw-8+S?eoWc%>@5NT?A^IJ;9F-oo-lN-(n0x;ds7V#WQBM!E9q~Y%z>&iuFA{sP9",
"6nr^GYX2V2|X)|#Ofa=StGG2a8RxoNO2ATYtgrfa0oU&?4XwfQaI{Pt)^;e#E?WiI#TzmB}={k}i",
"l4t3!OBGX;T3NqR1eQvKU+H2})GHKx~`^ckhg|}BxZern6tZ(urf>Nl*i(6p<!g9=1AS`G61mB<t",
"1L9n-F_-2Ms_Nz@*mHC$LlxEmT(onA)wJaii7iPksoSIgymz_h`-6;l7=?8(ABUNUl9LI*M_{fmK",
"g|$t41E#m3i*NisonntZFx&g^fQJPzSWSPHoGFQu58_E#MbR`Z254wqIo-T!gfZn4PSLq+%%HHC`",
"DS>r}E<FbY9rMk{BQpzcUJ#EU~iQE<d=d5xL=oP)zM{w_yZaYgd-=><1Z^J<PG}62x&9w~$yrT8Q",
"_)2TO0q{?MnlV6U4B;L7(ow=%w5Zsq1ZW;wi`qz=6qy`J1SR8;00sLZ-2Z=<sJl;q)w5c;B2(ee?",
"REDDvx7YM(ZJHALM{~&98!xlj5N{A&EVlWA=MzTK!eO^5NaeQPy<1NbQx;+b-n-gvHu^tr^--nGJ",
"ro{f3=fM>HUJRirei%pf0e-`iF?o=Gil{>&i{bRfwz2BhVIRCT#}|JdmOyct;C*G8@3`X<>O;$2<",
"%V00s!K~FHL834FK+9{ValUTh{1@nv?_pZ$BW^jj<`DJWW4z_;mxazJz2}EyA0dTSXv$w^$K_3?Y",
"~5aQ&82N&Hyl9sH4+uSWb(H|7hUoMVS-v#szXiFD7LTEG4j(k?U$a%`<f(+Zoe#s%}TPH0MgZgc}",
"Yhkx{>0q+w7(WKHq)?3ra>jCS;%n(_@`ZY<CNEM7+}cS}Yxppt9U$EtXTx#gWPlFv9bZ!-7|chL?",
"CFPNi%;Z~<XT$0&BYaQIOQ>wmubM@i<wb~A1k8OdXy@r5;aEGl`e&DRaWP{*gO8MI}JoU)H%(27M",
"w<G=*Gi|&O><@R?#Z*mu%5Tc|613%>+)$pN8Ju>MsvA|lc^l2d*{WWvu%8T0vEl5SIK$QVO%U(w)",
"m0PJ<Djewf^MF1lX6jA=MSoy>X1=_20;Lb*G!A=V;>gM930<q_C9VTK6mEdBsDyAL{8W358^K@<b",
"@7Ew{$7~6{hX2qqHEN)@Jc6@fgvJ1#>-?7xb%&#{`Q@v)rXj9jcJ)VK8&cAc-I2TJ<|fmdUya%7w",
"CSuk$d0f<SW3EtI0lb}lGPT#sP-$#i(Ze}EVM$%hT=Kj!%A*Yx{P`O3blS_`alcNe=6ySoD?+}%Z",
"P5Z~RY!-IOUq<=%i&4EfazJ8Z=YdKMi(k<78ith807<N!4q*!}Mu}jwZU6g!bDv!N}CFx57q&|yP",
"hsUQ7$4QN^Di=Eh0zPmIRq*(W9M*0P^!hJLgQ*7",
)
try:
 src=zlib.decompress(base64.b85decode("".join(P)))
except Exception as e:
 sys.exit("tiny-chess-01: corrupt packed engine: "+str(e))
exec(src)
