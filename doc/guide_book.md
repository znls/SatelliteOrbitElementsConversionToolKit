# 軌道要素とは
**〜Cartesian - Keplerian 相互変換の実装を目指して〜**

---

## 目次
- [軌道要素とは](#軌道要素とは)
  - [目次](#目次)
  - [軌道の基本](#軌道の基本)
  - [状況設定: 制限2体問題](#状況設定-制限2体問題)
  - [Cartesian軌道要素](#cartesian軌道要素)
  - [Keplerian軌道要素](#keplerian軌道要素)
    - [まとめ](#まとめ)
  - [Keplerian to Cartesian への変換](#keplerian-to-cartesian-への変換)
  - [演習問題](#演習問題)
---

## 軌道の基本
1. 楕円の幾何学
   1. 楕円の方程式
   2. 極座標系における楕円の方程式
2. 軌道のエネルギー積分
3. 練習問題

## 状況設定: 制限2体問題
1. 2体問題とは
2. 衛星の運動方程式
3. 角運動量ベクトル
4. 離心率ベクトル(ラプラスベクトル)
5. 2体問題の運動方程式の解析解
6. 練習問題

## Cartesian軌道要素
1. 位置ベクトルと速度ベクトル

## Keplerian軌道要素
1. 慣性座標系の導入
2. 軌道長半径($a$)
   1. $a$の定義
   2. 実装
3. 離心率($e$)
   1. $e$の定義
   2. 実装
4. 軌道傾斜角($i$)
   1. $i$ の定義
   2. 実装
5. 昇交点赤経($\Omega$)
   1. $\Omega$の定義
   2. 実装
6. 近地点引数($\omega$)
   1. $\omega$の定義
   2. 実装
7. True Anomaly($\nu$)
   1. $\nu$の定義
   2. 実装

### まとめ
- 軌道の形状を決める要素
- 軌道の慣性空間上の向きを決める要素
- 衛星の位置を決める要素

## Keplerian to Cartesian への変換
- 概要: ステップバイステップによる変換の流れ
- "Peri-focal"座標系の導入
- $\nu$を用いた衛星運動方程式
- Perifocal座標系における位置ベクトルと速度ベクトルの表現
- 回転行列とは
- ωの回転
- iの回転
- Ωの回転
- 練習問題


## 演習問題
- 軌道要素クラスの設計と実装