# bandit


## バンディット問題の理論とアルゴリズム
- https://www.kspub.co.jp/book/detail/1529175.html
- この本の7章の「LinUCB 方策」/トンプソンサンプリング、及Logistic regression ver.を実装している。



- thompson sampling の多変量正規分布からの乱数発生はhttps://analytics-note.xyz/programming/python-multivariate-normal-rvs/を参考にしました。
  乱数発生の方法でリグレットが変わってくるという記述があり、よくわかっていない。
<!-- 
https://blog.brainpad.co.jp/entry/2018/04/05/163000
こちらの実装をするためのレポジトリ
# Versions
- 2/12-19 まずは、モデルフリーアプローチで強化学習できるか？を実験してみる。
  - 以下の2つのレポジトリを参考にする。
  - https://github.com/icoxfog417/baby-steps-of-rl-ja/blob/master/DP/environment.py
  - https://github.com/Kaggle/kaggle-environments
-->

## Bandit_LinUCB.ipynb
- LinUCB法と、Thompson samplingの実装をしている。
- LinUCB法のアルゴリズムはこのnbでの実装を元に、Calculate_Regret.ipynbで更新・修正を行っているため、そちらを参照して欲しい。

## Calculate_Regret.ipynb

- LinUCB, Thompson sampling, UCB, $\epsilon$ - greedy法に基づく性能比較をするnb

## logistic_regression.ipynb

- Logit モデルに基づいたトンプソンサンプリングの実装
  ラプラス近似をしてthetaを数値計算するが、各iterationの度に逆行列を求める必要があり、online学習ではかなり時間がかかってしまうため、　thetaの更新を100回の試行ごとにしている。



# 今後の修正案

- Issuesで管理する。
