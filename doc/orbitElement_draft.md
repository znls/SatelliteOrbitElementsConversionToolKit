# 軌道要素とは


## 状況設定：制限2体問題(restricted two-body problem)
このノートの目標は，衛星の軌道要素についての理解とCartesian-Keplerian相互変換の実装である．従って，問題をシンプルにするため下記のような状況設定，すなわち「制限2体問題(restricted two-body problem)」について考える．

1. 座標系の導入
3. 制限(restricted)2体問題における衛星の運動方程式

### 座標系の導入: 地心赤道座標系(geocentric-equatorial coordinate system)
- 原点(Origin): 地心(center of the Earth);よって，**geocentric**
- 基準面(fundamental plane): 赤道(Earth's equator);よって，**geocentric-equatorial**
- 基準面に対する直角方向(perpendicular to plane): North Pole; $\hat{K}$
- Principal direction: 春分点方向(vernal equinox); $\hat{I}$
- Principal directionと基準面に対する直角方向から右手系を為す方向; $\hat{j}$

### 制限2体問題における衛星の運動方程式
2体問題(two-body problem)とは，2つの物体$P_1$，$P_2$の質量中心に対する相対運動を記述する問題であり，そのときの$P_1$に対する$P_2$の(あるいは$P_2$に対する$P_1$の)相対運動方程式は，
$$
\frac{d^2 \bold{r}}{dt^2} = - \frac{\mu}{r^3}\bold{r}
$$
ここで，$\mu$の定義が，万有引力定数$G$に対して．
$$
\mu \equiv G(m_1+m_2)
$$
であることを想起すると，$P_1$を地球，$P_2$を衛星としたときに，
$$
m_{1} >> m_{2}
$$
により，
$$
\mu \cong Gm_1
$$
よって，地球と衛星の質量中心まわりの運動は近似的に一致して，地球中心を質量原点にとってよい．これを「制限2体問題(restricted two-body problem)」と呼ぶ．

## 軌道運動の基本
ここでは，基本的な軌道運動(ケプラー運動)について復習する．まず楕円の幾何学について概観し．その後，Keplerian軌道要素への導入として，衛星の運動方程式から，軌道の力学的エネルギー，角運動量ベクトルや離心率ベクトルなどの概念を導入する．

1. 楕円の基本的なパラメータと楕円の極方程式
2. 角運動量ベクトル
3. 離心率ベクトル
4. 衛星運動方程式のエネルギー積分と長半径

**記法**：以降は太字(例えば，$\bold{r}$)はベクトルを表し，そうでなければ(例えば，$r$)はスカラーを表す．

### 1. 楕円の基本的なパラメータと楕円の極方程式

#### 離心率
離心率(eccentricity)とは，2つの焦点間の距離$2c$と楕円の長径$2a$の比として定義できる．
$$
e \equiv \frac{2c}{2a}
$$

#### 半直弦
半直弦(Semi-latus rectum)とは．焦点を通って長軸に垂直な弦の長さの半分であり，以下のように定義できる．
$$
p \equiv \frac{b^2}{a} = a(1-e^2)
$$

#### 楕円の極方程式
これらを用いて，楕円の極方程式は以下のように書ける．
$$
r(\nu) = \frac{p}{1+e\cos{\nu}}
$$

### 2. 角運動量ベクトル


### 3. 離心率ベクトル



### 4. 衛星運動方程式のエネルギー積分と長半径

#### エネルギー積分
単位質量あたりの運動エネルギーとポテンシャルエネルギーの和$\epsilon$が一定となる(2体系の全エネルギーが保存される)ことを示す．

衛星の運動方程式と$\dot{\bold{r}}$との内積
$$
\dot{\bold{r}} \cdot (\ddot{\bold{r}} + \frac{\mu}{r^3}) = 0
$$

から途中式は省略して，(see. 『ミッション解析と軌道設計の基礎』,pp.4-5 )　以下を得る．

$$
\frac{1}{2} \frac{d}{dt} (\bold{r} \cdot \bold{r}) + \frac{d}{dt} (- \frac{\mu}{\sqrt{\bold{r} \cdot \bold{r}}}) = 0
$$

これは直ちに積分できて，
$$
\frac{1}{2}(\dot{\bold{r}} \cdot \dot{\bold{r}}) - \frac{\mu}{r} = \epsilon \text{ (const)}
$$

これをエネルギー積分という．

なお，一般に
$$
\begin{align*}
\text{運動エネルギー} =  \frac{1}{2}mv^2 \\
\text{ポテンシャルエネルギー} = - \frac{m \mu}{r}
\end{align*}
$$
であり，力学的エネルギー$E$を運動エネルギーとポテンシャルエネルギーの和とおくと，
$$
E = \frac{1}{2}mv^2 - \frac{m \mu}{r}
$$
であり，これを単位質量$m$で割ったものを$\epsilon$と定義することで，本質的に同じ結果が得られる．
$$
\begin{align*}
\epsilon \equiv \frac{E}{m} \\
\end{align*}
$$
hence
$$
\epsilon = \frac{v^2}{2} - \frac{\mu}{r}
$$

#### 長半径$a$との関係
角運動量ベクトル$\bold{h}$と離心率ベクトル$\bold{P}$，および$\epsilon$の関係から，楕円の長半径$a$を$\epsilon$を用いて表すことができる．(see. 『ミッション解析と軌道設計の基礎』,pp.5-6,pp.20-21)
$$
a = - \frac{\mu}{2 \epsilon}
$$
ここから，長半径$a$は軌道のエネルギー$\epsilon$のみによって決まることが分かる．
