# Part of Spatial Math Toolbox for Python
# Copyright (c) 2000 Peter Corke
# MIT Licence, see details in top-level file: LICENCE

from spatialmath.base.argcheck import *  # lgtm [py/polluting-import]
from spatialmath.base.quaternions import *  # lgtm [py/polluting-import]
from spatialmath.base.transforms2d import *  # lgtm [py/polluting-import]
from spatialmath.base.transforms3d import *  # lgtm [py/polluting-import]
from spatialmath.base.transformsNd import *  # lgtm [py/polluting-import]
from spatialmath.base.vectors import *  # lgtm [py/polluting-import]
from spatialmath.base.symbolic import *  # lgtm [py/polluting-import]
from spatialmath.base.animate import *  # lgtm [py/polluting-import]
from spatialmath.base.graphics import *  # lgtm [py/polluting-import]
from spatialmath.base.numeric import *  # lgtm [py/polluting-import]

# from spatialmath.base.argcheck import (
#     assertmatrix,
#     ismatrix,
#     getvector,
#     assertvector,
#     isvector,
#     isscalar,
#     getunit,
#     isnumberlist,
#     isvectorlist,
# )
# from spatialmath.base.quaternions import (
#     pure,
#     qnorm,
#     unit,
#     isunit,
#     isequal,
#     q2v,
#     v2q,
#     qqmul,
#     inner,
#     qvmul,
#     vvmul,
#     qpow,
#     conj,
#     q2r,
#     r2q,
#     slerp,
#     rand,
#     matrix,
#     dot,
#     dotb,
#     angle,
#     qprint,
# )
# from spatialmath.base.transforms2d import (
#     rot2,
#     trot2,
#     transl2,
#     ishom2,
#     isrot2,
#     trlog2,
#     trexp2,
#     tr2jac2,
#     trinterp2,
#     trprint2,
#     trplot2,
#     tranimate2,
#     xyt2tr,
#     tr2xyt,
#     trinv2,
# )
# from spatialmath.base.transforms3d import (
#     rotx,
#     roty,
#     rotz,
#     trotx,
#     troty,
#     trotz,
#     transl,
#     ishom,
#     isrot,
#     rpy2r,
#     rpy2tr,
#     eul2r,
#     eul2tr,
#     angvec2r,
#     angvec2tr,
#     exp2r,
#     exp2tr,
#     oa2r,
#     oa2tr,
#     tr2angvec,
#     tr2eul,
#     tr2rpy,
#     trlog,
#     trexp,
#     trnorm,
#     trinterp,
#     delta2tr,
#     trinv,
#     tr2delta,
#     tr2jac,
#     rpy2jac,
#     eul2jac,
#     exp2jac,
#     rot2jac,
#     angvelxform,
#     trprint,
#     trplot,
#     tranimate,
# )
# from spatialmath.base.transformsNd import (
#     t2r,
#     r2t,
#     tr2rt,
#     rt2tr,
#     Ab2M,
#     isR,
#     isskew,
#     isskewa,
#     iseye,
#     skew,
#     vex,
#     skewa,
#     vexa,
#     h2e,
#     e2h,
#     homtrans,
#     rodrigues,
# )
# from spatialmath.base.vectors import (
#     colvec,
#     unitvec,
#     unitvec_norm,
#     norm,
#     normsq,
#     isunitvec,
#     iszerovec,
#     isunittwist,
#     isunittwist2,
#     unittwist,
#     unittwist_norm,
#     unittwist2,
#     angdiff,
#     removesmall,
#     cross,
#     iszero,
#     wrap_0_2pi,
#     wrap_mpi_pi,
# )
# from spatialmath.base.symbolic import *
# from spatialmath.base.animate import Animate, Animate2
# from spatialmath.base.graphics import (
#     plotvol2,
#     plotvol3,
#     plot_point,
#     plot_text,
#     plot_box,
#     plot_poly,
#     circle,
#     ellipse,
#     sphere,
#     ellipsoid,
#     plot_box,
#     plot_circle,
#     plot_ellipse,
#     plot_homline,
#     plot_sphere,
#     plot_ellipsoid,
#     plot_cylinder,
#     plot_cone,
#     plot_cuboid,
#     axes_logic,
#     isnotebook,
# )
# from spatialmath.base.numeric import numjac, array2str, bresenham


__all__ = [
    # spatialmath.base.argcheck
    "assertmatrix",
    "ismatrix",
    "getvector",
    "assertvector",
    "isvector",
    "isscalar",
    "getunit",
    "isnumberlist",
    "isvectorlist",
    # spatialmath.base.quaternions
    "pure",
    "qnorm",
    "unit",
    "isunit",
    "isequal",
    "q2v",
    "v2q",
    "qqmul",
    "inner",
    "qvmul",
    "vvmul",
    "qpow",
    "conj",
    "q2r",
    "r2q",
    "slerp",
    "rand",
    "matrix",
    "dot",
    "dotb",
    "angle",
    "qprint",
    # spatialmath.base.transforms2d
    "rot2",
    "trot2",
    "transl2",
    "ishom2",
    "isrot2",
    "trlog2",
    "trexp2",
    "tr2jac2",
    "trinterp2",
    "trprint2",
    "trplot2",
    "tranimate2",
    "xyt2tr",
    "tr2xyt",
    "trinv2",
    # spatialmath.base.transforms3d
    "rotx",
    "roty",
    "rotz",
    "trotx",
    "troty",
    "trotz",
    "transl",
    "ishom",
    "isrot",
    "rpy2r",
    "rpy2tr",
    "eul2r",
    "eul2tr",
    "angvec2r",
    "angvec2tr",
    "exp2r",
    "exp2tr",
    "oa2r",
    "oa2tr",
    "tr2angvec",
    "tr2eul",
    "tr2rpy",
    "trlog",
    "trexp",
    "trnorm",
    "trinterp",
    "delta2tr",
    "trinv",
    "tr2delta",
    "tr2jac",
    "rpy2jac",
    "eul2jac",
    "exp2jac",
    "rot2jac",
    "angvelxform",
    "angvelxform_dot",
    "trprint",
    "trplot",
    "tranimate",
    "tr2x",
    "x2tr",
    # spatialmath.base.transformsNd
    "t2r",
    "r2t",
    "tr2rt",
    "rt2tr",
    "Ab2M",
    "isR",
    "isskew",
    "isskewa",
    "iseye",
    "skew",
    "vex",
    "skewa",
    "vexa",
    "h2e",
    "e2h",
    "homtrans",
    "rodrigues",
    # spatialmath.base.vectors
    "colvec",
    "unitvec",
    "unitvec_norm",
    "norm",
    "normsq",
    "isunitvec",
    "iszerovec",
    "isunittwist",
    "isunittwist2",
    "unittwist",
    "unittwist_norm",
    "unittwist2",
    "angdiff",
    "removesmall",
    "cross",
    "iszero",
    "wrap_0_2pi",
    "wrap_mpi_pi",
    # spatialmath.base.animate
    "Animate",
    "Animate2",
    # spatial.base.graphics
    "plotvol2",
    "plotvol3",
    "plot_point",
    "plot_text",
    "plot_box",
    "plot_poly",
    "circle",
    "ellipse",
    "sphere",
    "ellipsoid",
    "plot_box",
    "plot_circle",
    "plot_ellipse",
    "plot_homline",
    "plot_sphere",
    "plot_ellipsoid",
    "plot_cylinder",
    "plot_cone",
    "plot_cuboid",
    "axes_logic",
    "isnotebook",
    # spatial.base.numeric
    "numjac",
    "numhess",
    "array2str",
    "bresenham",
]
