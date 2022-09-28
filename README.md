# setup on macOS
## pre-requisites
* Install `macFUSE` https://macfuse.io
    ```
    brew install macfuse
    ```
* Install `just` command runner https://github.com/casey/just
    ```
    brew install just
    ```
* Install `go`
    ```
    brew install go
    ```
# build litefs from source
* clone litefs repo
  ```bash
  # this fork supports macOS, and the official repo doesn't support macOS yet 
  # https://github.com/superfly/litefs/issues/119
  git clone git@github.com:anacrolix/litefs.git
  ```

* Build `litefs`
```bash
# this will compile litefs binary and install it into /usr/local/bin
go build -ldflags "-s -w -X 'main.Version=latest' -extldflags '-static'" -tags osusergo,netgo,sqlite_omit_load_extension -o /usr/local/bin/litefs ./cmd/litefs
```

# setup litefs cluster
* create `.env` file under this testbed root folder with content like below
```
LITEFS_NODES_DIR = ${HOME}/path/to/your/litefs_testbed/nodes
```
* start litefs cluster
A two-node cluster will be setup. The primary node is static (no `Consul` required).

```bash
# start node 1 (primary node) in the 1st terminal
just start n1

# start node 2 (replica node) in the 2nd terminal
just start n2
```
* play with the litefs
```bash
# write some data into node 1
just app

# view replicated data in node 2
# this will launch sqlite shell
# you can run `SELECT * FROM movie;` to view the data
# this is a read-only replica, so you are not expected to write data into it
just db n2

# view the folder structure (LXT files/data folder/mnt folder)
tree .
```