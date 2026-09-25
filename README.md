<div align="center">
  <img src="assets/hero.svg" width="100%" alt="SOCKS7 — Next Generation Encrypted Proxy Protocol"/>
</div>

<br/>

<div align="center">

> **𝑆𝑂𝐶𝐾𝑆7** is not "another proxy". It is a ground-up transport fabric that carries *many* logical streams over a *single* obfuscated socket — with a 2-RTT zero-knowledge handshake, forward secrecy, and automatic least-latency egress failover.

</div>

<br/>

## ⚡ 𝑆𝑒𝑒 𝑖𝑡 𝑚𝑜𝑣𝑒

<div align="center">
  <img src="assets/terminal.svg" width="92%" alt="socks7 live terminal session"/>
</div>

<br/>

## 🧬 𝑊ℎ𝑦 𝑆𝑂𝐶𝐾𝑆7 𝑒𝑥𝑖𝑠𝑡𝑠

|  | Classic SOCKS5 | **𝑆𝑂𝐶𝐾𝑆7** |
|---|---|---|
| Streams per connection | 1 | **unlimited (multiplexed)** |
| Handshake | plaintext negotiation | **2-RTT zero-knowledge** |
| Key exchange | none | **ephemeral X25519 + PSK** |
| Cipher suite | none / external | **XChaCha20-Poly1305** |
| UDP | awkward | **native, first-class** |
| Failover | manual | **automatic, least-latency** |
| Fingerprint | obvious | **obfuscated (TLS 1.3 cover)** |

<br/>

<div align="center">
  <img src="assets/topology.svg" width="100%" alt="SOCKS7 multiplexed tunnel topology"/>
</div>

<br/>

## 🔐 𝑇ℎ𝑒 ℎ𝑎𝑛𝑑𝑠ℎ𝑎𝑘𝑒

<div align="center">
  <img src="assets/handshake.svg" width="100%" alt="SOCKS7 handshake sequence"/>
</div>

<br/>

## 📡 𝐿𝑖𝑣𝑒 𝑡𝑒𝑙𝑒𝑚𝑒𝑡𝑟𝑦

<div align="center">
  <img src="assets/metrics.svg" width="100%" alt="SOCKS7 live telemetry dashboard"/>
</div>

<br/>

## 🌐 𝑇ℎ𝑒 𝑓𝑎𝑏𝑟𝑖𝑐

<div align="center">
  <img src="assets/contribution-network.svg" width="100%" alt="SOCKS7 contribution network"/>
</div>

<br/>

## 🧰 𝑄𝑢𝑖𝑐𝑘 𝑠𝑡𝑎𝑟𝑡

```bash
# 1 · install
curl -fsSL https://socks7.dev/install.sh | sh

# 2 · spin up a local edge node
socks7 node --listen :1080 --cipher xchacha20 --obfs tls1.3

# 3 · route any client through the fabric
socks7 connect --peer edge-1.eu --streams 4
```

```python
from socks7 import Client

with Client("127.0.0.1:1080", streams=8) as c:
    for host in ("api.example.com", "cdn.example.com"):
        c.get(f"https://{host}/")   # multiplexed over one socket
```

<br/>

## 🗺 𝑅𝑜𝑎𝑑𝑚𝑎𝑝

```text
[x]  v7.0  core transport · mux · XChaCha20            <- shipping
[ ]  v7.1  QUIC datagram mode · 0-RTT resume
[ ]  v7.2  pluggable transports marketplace
[ ]  v7.3  hardware offload + kernel bypass (io_uring)
[ ]  v8.0  post-quantum hybrid KEM (X25519 + Kyber)
```

<br/>

## 🔗 𝐶𝑜𝑛𝑛𝑒𝑐𝑡

<div align="center">
  <img src="assets/badges.svg" width="720" alt="SOCKS7 badges"/>
</div>

<div align="center">

[**socks7.dev**](#) &nbsp;·&nbsp; [**Docs**](#) &nbsp;·&nbsp; [**Releases**](#) &nbsp;·&nbsp; [**Discussions**](#)

</div>

<div align="center">
  <sub><code>// 𝑏𝑢𝑖𝑙𝑡 𝑜𝑛𝑒 𝑝𝑎𝑐𝑘𝑒𝑡 𝑎𝑡 𝑎 𝑡𝑖𝑚𝑒 · 𝑆𝑂𝐶𝐾𝑆7 © 2026</code></sub>
</div>
