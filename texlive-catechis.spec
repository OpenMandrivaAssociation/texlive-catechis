%global tl_name catechis
%global tl_revision 59998

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6
Release:	%{tl_revision}.1
Summary:	Macros for typesetting catechisms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/catechis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catechis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The macros include: format for question-and-answer; comments on answers;
lengthier explanations of answers; citations. The formatting of all the
macros is highly (and simply) customizable.

